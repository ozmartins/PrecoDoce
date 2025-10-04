from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_POST, require_GET
from .models import Fornecedor
from .forms import FornecedorForm


@require_GET
def fornecedor_listar(request):
    q = request.GET.get('q', '')
    qs = Fornecedor.objects.all().order_by("nome")
    if q:
        qs = qs.filter(nome__icontains=q)    
    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))    
    return render(request, "fornecedor/listar.html", {
        "fornecedores": page_obj.object_list,
        "page_obj": page_obj,
    })


@require_POST
def fornecedor_cadastrar(request):
    form = FornecedorForm(request.POST)
    if form.is_valid():
        fornecedor = form.save()        
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse(
                {"ok": True, "id": fornecedor.pk, "nome": fornecedor.nome},
                status=201
            )        
        messages.success(request, "Fornecedor cadastrado com sucesso.")
        return redirect("compra:fornecedor_listar")
    
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)

    messages.success(request, "Fornecedor cadastrado com sucesso.")
    return redirect("compra:fornecedor_listar")


@require_POST
def fornecedor_alterar(request, pk: int):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    form = FornecedorForm(request.POST, instance=fornecedor)
    if form.is_valid():
        fornecedor = form.save()

        # Resposta JSON (para AJAX)
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "ok": True,
                "id": fornecedor.pk,
                "nome": fornecedor.nome,
            })

        # Navegação tradicional
        messages.success(request, "Fornecedor atualizado com sucesso.")
        return redirect("compra:fornecedor_listar")

    # Erros de validação
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)

    return redirect("compra:fornecedor_listar")


@require_POST
def fornecedor_remover(request, pk: int):        
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"ok": True, "id": pk})
    messages.success(request, "Fornecedor excluído com sucesso.")
    return redirect("compra:fornecedor_listar")