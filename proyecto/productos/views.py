from django.shortcuts import render


# Create your views here.
def bienvenida(request):
    return render(
        request=request,
        template_name="bienvenida.html",
        context={
            "message": "This is a context message",
            "products": [
                {
                    "type": "tv",
                    "vendor": "LG",
                    "name": "LG OLED",
                    "description": "LG OLED",
                    "thumbnail": "",
                },
                {
                    "name": "Radio"
                },
                {
                    "name": "Phone"
                },
            ],
            "error": "Some shit happens"
        })
