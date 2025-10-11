from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST, require_GET

from ..models import Supplier
from ..forms import SupplierForm
from .utils import is_ajax

@require_GET
def supplier_recover(request):
    q = request.GET.get("q", "")
    qs = Supplier.objects.all().order_by("name")
    if q:
        qs = qs.filter(name__icontains=q)
    page_obj = Paginator(qs, 10).get_page(request.GET.get("page"))
    return render(request, "supplier.html", {
        "suppliers": page_obj.object_list,
        "page_obj": page_obj,
    })

@require_POST
def supplier_create(request):
    form = SupplierForm(request.POST)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        return render(request, "supplier.html", status=400)

    supplier = form.save()
    if is_ajax(request):
        return JsonResponse({"ok": True, "id": supplier.pk, "name": supplier.name})
    return redirect("purchases:supplier_recover")

@require_POST
def supplier_update(request, pk: int):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST, instance=supplier)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({"ok": False, "errors": form.errors}, status=400)
        return render(request, "supplier.html", status=400)

    supplier = form.save()
    if is_ajax(request):
        return JsonResponse({"ok": True, "id": supplier.pk, "name": supplier.name})
    return redirect("purchases:supplier_recover")

@require_POST
def supplier_delete(request, pk: int):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    if is_ajax(request):
        return JsonResponse({"ok": True})
    return redirect("purchases:supplier_recover")
