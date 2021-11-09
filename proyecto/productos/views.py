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
    productos.filter(precio__gte=10000).delete()

    return render(
        request=request,
        template_name="bienvenida.html",
        context={
            "message": "This is a context message",
            "productos": productos,
            "productos_filtrados": productos_filtrados
            # "error": "Some shit happens"
        })
