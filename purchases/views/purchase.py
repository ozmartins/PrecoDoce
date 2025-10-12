from django.db import transaction
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from ..models import Purchase, PurchaseItem, Supplier, Ingredient
from ..forms import PurchaseForm
from .utils import is_ajax
import json

def _items_qs(purchase: Purchase):    
    return (purchase.purchaseitem_set
            .select_related("ingredient")
            .order_by("id"))

@require_GET
def purchase_recover(request):    
    q = request.GET.get("q", "")    
    qs = (Purchase.objects
          .select_related("supplier")
          .order_by("-date"))            
    if q:        
        qs = qs.filter(supplier_id__name__icontains=q)        
    page_obj = Paginator(qs, 10).get_page(request.GET.get("page"))        
    return render(request, "purchase/index.html", {
        "purchases": page_obj.object_list,
        "page_obj": page_obj,
    })

@require_http_methods(["GET", "POST"])
def purchase_create(request):
    if request.method == "GET":
        suppliers = Supplier.objects.order_by("name")
        ingredients = Ingredient.objects.order_by("name")
        context = {
            "suppliers": suppliers,
            "ingredients": ingredients,
        }
        return render(request, "purchase/create.html", context)
    
    form = PurchaseForm(request.POST)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        suppliers = Supplier.objects.order_by("name")
        ingredients = Ingredient.objects.order_by("name")
        context = {
            "form": form,
            "suppliers": suppliers,
            "ingredients": ingredients,
        }
        return render(request, "purchase/create.html", context, status=400)

    try:
        with transaction.atomic():
            purchase = form.save(commit=False)
            purchase.total = 0
            purchase.date = purchase.date or timezone.now()
            purchase.save()
            
            items_json = request.POST.get("items_json", "[]")
            items_data = json.loads(items_json)

            for item in items_data:
                ingredient = Ingredient.objects.get(pk=item["ingredient_id"])
                PurchaseItem.objects.create(
                    purchase=purchase,
                    ingredient=ingredient,
                    quantity=item["quantity"],
                    metric_system_unit=item["metric_system_unit"],
                    total=item["total"]
                )
            
            total_sum = sum(i["total"] for i in items_data)
            print("total_sum=",total_sum)
            purchase.total = total_sum
            purchase.save()

    except Exception as e:
        if is_ajax(request):
            return JsonResponse({"ok": False, "error": str(e)}, status=400)
        suppliers = Supplier.objects.order_by("name")
        ingredients = Ingredient.objects.order_by("name")
        return render(request, "purchase/create.html", {
            "form": form,
            "suppliers": suppliers,
            "ingredients": ingredients,
            "error_message": str(e)
        }, status=400)

    if is_ajax(request):
        return JsonResponse({"ok": True, "id": purchase.pk})

    return redirect("purchases:purchase_recover")

@require_http_methods(["GET", "POST"])
def purchase_update(request, pk: int):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == "GET":
        form = PurchaseForm(instance=purchase)
        items = _items_qs(purchase)
        return render(
            request,
            "purchase/update.html",
            {"form": form, "purchase": purchase, "purchase_items": items},
        )


    form = PurchaseForm(request.POST, instance=purchase)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        items = _items_qs(purchase)
        return render(
            request,
            "purchase/update.html",
            {"form": form, "purchase": purchase, "purchase_items": items},
            status=400,
        )

    try:
        with transaction.atomic():
            purchase = form.save(commit=False)
            purchase.date = purchase.date or timezone.now()
            purchase.total = 0
            purchase.save()
            
            items_json = request.POST.get("items_json", "[]")
            items_data = json.loads(items_json)
            
            purchase.purchaseitem_set.all().delete()

            for item in items_data:                
                ingredient = Ingredient.objects.get(pk=item["ingredient_id"])                
                PurchaseItem.objects.create(
                    purchase=purchase,
                    ingredient=ingredient,
                    quantity=item["quantity"],
                    metric_system_unit=item["metric_system_unit"],
                    total=item["total"],
                )
            
            total_sum = sum((i.get("total") or 0) for i in items_data)
            purchase.total = total_sum
            purchase.save()

    except Exception as e:
        if is_ajax(request):
            return JsonResponse({"ok": False, "error": str(e)}, status=400)        
        items = _items_qs(purchase)
        return render(
            request,
            "purchase/update.html",
            {
                "form": form,
                "purchase": purchase,
                "purchase_items": items,
                "error_message": str(e),
            },
            status=400,
        )

    if is_ajax(request):
        return JsonResponse({"ok": True, "id": purchase.pk})

    return redirect("purchases:purchase_recover")


@require_POST
def purchase_delete(request, pk: int):
    purchase = get_object_or_404(Purchase, pk=pk)
    purchase.delete()
    if is_ajax(request):
        return JsonResponse({"ok": True})
    return redirect("purchases:purchase_recover")
