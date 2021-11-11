from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("bienvenida")
        
        return render(request, "login.html", context={"error": "Fallo al authenticar"})

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password)
        user.first_name = first_name
        user.save()
        login(request, user)

        return redirect("bienvenida")
    return render(request, "register.html")