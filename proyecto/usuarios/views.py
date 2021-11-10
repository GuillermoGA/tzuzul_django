from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "bienvenida.html")
        
        return render(request, "login.html", context={"error": "Fallo al authenticar"})

    return render(request, "login.html")