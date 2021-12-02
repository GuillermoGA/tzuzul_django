from django.shortcuts import render
import csv
# Create your views here.
def datos_usuarios(request):
    try:
        with open('./usuarios/marketing_campaign.csv') as csv_file:
            csv_data = csv.reader(csv_file)

            for line in csv_data:
                print(line)
    except (IOError, OSError) as file_error:
        print("No se puede abrir el archivo")
    return render(request, 'datos_usuarios.html')