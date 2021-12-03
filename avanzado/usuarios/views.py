from django.shortcuts import render
import csv
from django.core.files.storage import FileSystemStorage
# Create your views here.


def datos_usuarios(request):
    if request.method == "POST":
        file = request.FILES["archivo"]
        try:
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            csv_file = open(fs.path(filename))
            csv_data = csv.reader(csv_file, delimiter='\t')

            for line in csv_data:
                print(line)
        except (IOError, OSError) as file_error:
            print(f"No se puede abrir el archivo. {file_error}")

    try:
        with open('./usuarios/marketing_campaign.csv') as csv_file:
            csv_data = csv.reader(csv_file, delimiter='\t')

            data = []
            for line in csv_data:
                data.append(line)

    except (IOError, OSError) as file_error:
        print(f"No se puede abrir el archivo. {file_error}")
    return render(request, 'datos_usuarios.html', {"data": data})
