from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST, require_GET

from ..models import Ingredient
from ..forms import IngredientForm  
from .utils import is_ajax

@require_GET
def ingredient_recover(request):
    q = request.GET.get("q", "")
    qs = Ingredient.objects.all().order_by("name")
    if q:
        qs = qs.filter(name__icontains=q)
    page_obj = Paginator(qs, 10).get_page(request.GET.get("page"))
    return render(request, "ingredient.html", {
        "ingredients": page_obj.object_list,
        "page_obj": page_obj,
    })

@require_POST
def ingredient_create(request):
    form = IngredientForm(request.POST)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        return render(request, "ingredient.html", status=400)

    ingredient = form.save()
    if is_ajax(request):
        return JsonResponse({"ok": True, "id": ingredient.pk, "name": ingredient.name})
    return redirect("purchases:ingredient_recover")

@require_POST
def ingredient_update(request, pk: int):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    form = IngredientForm(request.POST, instance=ingredient)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        return render(request, "ingredient.html", status=400)

    ingredient = form.save()
    if is_ajax(request):
        return JsonResponse({"ok": True, "id": ingredient.pk, "name": ingredient.name})
    return redirect("purchases:ingredient_recover")

@require_POST
def ingredient_delete(request, pk: int):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    ingredient.delete()
    if is_ajax(request):
        return JsonResponse({"ok": True})
    return redirect("purchases:ingredient_recover")

@require_GET
def ingredient_search(request):
    q = (request.GET.get("q") or "").strip()
    results = []
    if q:
        qs = Ingredient.objects.filter(name__icontains=q).order_by("name")[:10]
        results = [{"id": s.id, "name": s.name} for s in qs]
    return JsonResponse({"results": results})
