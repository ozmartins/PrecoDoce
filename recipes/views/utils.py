from django.http import JsonResponse

def is_ajax(request):
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"

def json_or_4xx(form, template_name):
    if is_ajax(form.request):
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)    
    from django.shortcuts import render
    return render(form.request, template_name, status=400)