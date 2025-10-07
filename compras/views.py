from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST, require_GET
from .models import Fornecedor, Insumo
from .forms import FornecedorForm

def _is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


# --- FORNECEDORES ---

@require_GET
def fornecedor_listar(request):
    q = request.GET.get('q', '')
    qs = Fornecedor.objects.all().order_by('nome')
    if q:
        qs = qs.filter(nome__icontains=q)
    page_obj = Paginator(qs, 10).get_page(request.GET.get('page'))
    return render(request, 'fornecedor.html', {
        'fornecedores': page_obj.object_list,
        'page_obj': page_obj,
    })

@require_POST
def fornecedor_cadastrar(request):
    form = FornecedorForm(request.POST)
    if not form.is_valid():
        if _is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
        # fallback (se quiser suportar navegação tradicional):
        return render(request, 'fornecedor.html', status=400)  # ajuste conforme sua UX
    fornecedor = form.save()
    if _is_ajax(request):
        return JsonResponse({'ok': True, 'id': fornecedor.pk, 'nome': fornecedor.nome})
    # fallback:
    return redirect('compra:fornecedor_listar')

@require_POST
def fornecedor_alterar(request, pk: int):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST, instance=fornecedor)
    if not form.is_valid():
        if _is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
        return render(request, 'fornecedor.html', status=400)
    fornecedor = form.save()
    if _is_ajax(request):
        return JsonResponse({'ok': True, 'id': fornecedor.pk, 'nome': fornecedor.nome})
    return redirect('compra:fornecedor_listar')

@require_POST
def fornecedor_remover(request, pk: int):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    if _is_ajax(request):
        return JsonResponse({'ok': True})
    return redirect('compra:fornecedor_listar')


# --- INSUMOS ---

@require_GET
def insumo_listar(request):
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
    form = FornecedorForm(request.POST)
    if not form.is_valid():
        if _is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
        # fallback (se quiser suportar navegação tradicional):
        return render(request, 'fornecedor.html', status=400)  # ajuste conforme sua UX
    fornecedor = form.save()
    if _is_ajax(request):
        return JsonResponse({'ok': True, 'id': fornecedor.pk, 'nome': fornecedor.nome})
    # fallback:
    return redirect('compra:insumo_listar')

@require_POST
def insumo_alterar(request, pk: int):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST, instance=fornecedor)
    if not form.is_valid():
        if _is_ajax(request):
            return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
        return render(request, 'fornecedor.html', status=400)
    fornecedor = form.save()
    if _is_ajax(request):
        return JsonResponse({'ok': True, 'id': fornecedor.pk, 'nome': fornecedor.nome})
    return redirect('compra:insumo_listar')

@require_POST
def insumo_remover(request, pk: int):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    if _is_ajax(request):
        return JsonResponse({'ok': True})
    return redirect('compra:insumo_listar')