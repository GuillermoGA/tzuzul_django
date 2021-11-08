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
                    "description": "The new LG OLED super power mola mogollon",
                    "thumbnail": r"img\tv_lg_oled_55.png",
                },
                {
                    "type": "phone",
                    "vendor": "Apple",
                    "name": "iPhone 13 Pro Max",
                    "description": "The new iPhone super power mola mogollon",
                    "thumbnail": r"img\iphone_13_pro_max.jpg",
                },
            ],
            # "error": "Some shit happens"
        })
