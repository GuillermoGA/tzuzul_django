import csv
import tempfile
from io import StringIO

from django.shortcuts import render

from .models import Usuario


def datos_usuarios(request):
    if request.method == "POST":
        file = request.FILES["archivo"]
        try:
            # Create temp file
            tmp_file = tempfile.mkstemp()[1]

            # Read data from file
            file_data = file.read()

            # Store data in temp file
            with open(tmp_file, "w+b") as f:
                f.write(file_data)

            csv_data = []
            # Read csv from temp file
            with open(tmp_file) as csv_file:
                # Read csv from buffer
                csv_data = csv.reader(csv_file)

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


# Using InMemoryUploadedFile
def __read_in_memory_csv(file):
    """ Read csv file directly from memory """
    # Get InMemoryUploadedFile data in bytes
    file_data = file.read()

    # Cast bytes to string by decoding in UTF-8
    str_file_data = file_data.decode("UTF-8")

    # Create buffer from string
    file_data_buffer = StringIO(str_file_data)

    # Read csv from buffer
    csv_data = csv.reader(file_data_buffer)

    return csv_data
