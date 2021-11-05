from django.shortcuts import render


# Create your views here.
def bienvenida(request):
    return render(
        request=request,
        template_name="bienvenida.html",
        context={
            "message": "This is a context message",
            "products": ["TV", "Radio", "Phone"],
            "error": "Some shit happens"
        })
