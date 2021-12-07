import csv
from io import StringIO

from django.shortcuts import render

from .models import Usuario


def datos_usuarios(request):
    if request.method == "POST":
        file = request.FILES["archivo"]
        try:
            # Get InMemoryUploadedFile data in bytes
            file_data = file.read()

            # Cast bytes to string by decoding in UTF-8
            str_file_data = file_data.decode("UTF-8")

            # Create buffer from string
            file_data_buffer = StringIO(str_file_data)

            # Read csv from buffer
            csv_data = csv.reader(file_data_buffer)

            for line in csv_data:
                Usuario.objects.create(
                    id=line[0],
                    year_birth=line[1],
                    education=line[2],
                    income=line[4]
                )
        except (IOError, OSError) as file_error:
            print(f"No se puede abrir el archivo. {file_error}")
        except Exception as e:
            print(f"Unknown error: {e}")

    data = Usuario.objects.all()
    return render(request, 'datos_usuarios.html', {"data": data})
