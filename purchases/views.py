from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST, require_GET
from .models import Supplier, Insumo
from .forms import SupplierForm


def is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


@require_GET
def supplier_recover(request):
    q = request.GET.get('q', '')
    qs = Supplier.objects.all().order_by('nome')
    if q:
        qs = qs.filter(nome__icontains=q)
    page_obj = Paginator(qs, 10).get_page(request.GET.get('page'))
    return render(request, 'supplier.html', {
        'suppliers': page_obj.object_list,
        'page_obj': page_obj,
    })

@require_POST
def supplier_cadastrar(request):
    form = SupplierForm(request.POST)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)        
        return render(request, 'supplier.html', status=400)  
    supplier = form.save()
    if is_ajax(request):
        return JsonResponse({'ok': True, 'id': supplier.pk, 'nome': supplier.nome})
    return redirect('purchases:supplier_recover')

@require_POST
def supplier_alterar(request, pk: int):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST, instance=supplier)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
        return render(request, 'supplier.html', status=400)
    supplier = form.save()
    if is_ajax(request):
        return JsonResponse({'ok': True, 'id': supplier.pk, 'nome': supplier.nome})
    return redirect('purchases:supplier_recover')

@require_POST
def supplier_remover(request, pk: int):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    if is_ajax(request):
        return JsonResponse({'ok': True})
    return redirect('purchases:supplier_recover')


# --- INSUMOS ---

@require_GET
def insumo_recover(request):
    q = request.GET.get('q', '')
    qs = Insumo.objects.all().order_by('nome')
    if q:
        qs = qs.filter(nome__icontains=q)
    page_obj = Paginator(qs, 10).get_page(request.GET.get('page'))
    return render(request, 'insumo.html', {
        'insumos': page_obj.object_list,
        'page_obj': page_obj,
    })

@require_POST
def insumo_cadastrar(request):
    form = SupplierForm(request.POST)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)        
        return render(request, 'supplier.html', status=400)  
    supplier = form.save()
    if is_ajax(request):
        return JsonResponse({'ok': True, 'id': supplier.pk, 'nome': supplier.nome})

    return redirect('purchases:insumo_recover')

@require_POST
def insumo_alterar(request, pk: int):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST, instance=supplier)
    if not form.is_valid():
        if is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
        return render(request, 'supplier.html', status=400)
    supplier = form.save()
    if is_ajax(request):
        return JsonResponse({'ok': True, 'id': supplier.pk, 'nome': supplier.nome})
    return redirect('purchases:insumo_recover')

@require_POST
def insumo_remover(request, pk: int):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    if is_ajax(request):
        return JsonResponse({'ok': True})
    return redirect('purchases:insumo_recover')