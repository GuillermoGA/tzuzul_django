from django.shortcuts import render
from .models import Producto

# Create your views here.
def bienvenida(request):

    # SELECT * FROM productos
    productos = Producto.objects.all()


    # SELECT * FROM productos WHERE precio < 5000
    productos_filtrados = Producto.objects.filter(precio__lte=9000)

    # Crear un formulario, los campos necesarios

    # INSERT INTO productos VALUES()
    Producto.objects.create(
        nombre="Consola", 
        precio=8000, 
        descripcion="Una consola", 
        cantidad=10)

    # UPDATE productos WHERE ---
    productos_filtrados.update(precio=5000)

    # DELETE productos WHERE ---
    productos.filter(precio__gte=6000).delete()

    return render(
        request=request,
        template_name="bienvenida.html",
        context={
            "message": "This is a context message",
            "productos": productos,
            "productos_filtrados": productos_filtrados
            # "error": "Some shit happens"
        })

def formulario(request):
    if request.method == "POST":
        nombre=request.POST["nombre"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        print(nombre)
        print(descripcion)
        print(precio)

        if nombre == "":
            print("Nombre vacio")
            return render(request, "formulario.html", context={"errors": ["El nombre no puede estar vacio"]})

        Producto.objects.create(
            nombre=nombre, 
            precio=precio, 
            descripcion=descripcion)
            
        return render(request, "bienvenida.html")
    return render(request, "formulario.html")