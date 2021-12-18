# FROM Definir la imagen base
# RUN Definimos el comando de inicio
# CMD Similar a RUN, pero se ejecuta despues de instaciar el contenedor
# ENTRYPOINT Seleccionamos la aplicacion por defecto de la imagen
# WORKDIR Similar a un cd
# ADD Copia archivos de la fuente (proyecto) adentro del contenedor
# ENV Define las variables de entorno

FROM python:latest

WORKDIR /src

# COPY requirements.txt /src/
COPY requirements.txt .

RUN pip install -r requirements.txt

# COPY . /src/
COPY . .

# CMD "python manage.py runserver"
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]