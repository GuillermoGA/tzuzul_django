from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto:", max_length=50)
    cantidad = forms.IntegerField()
    precio = forms.FloatField()
    descripcion = forms.CharField(widget=forms.Textarea)
