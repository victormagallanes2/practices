# Django Modules

  ERP


# Tecnologias usadas para este proyecto

  Django 2.2.3, Python >3.5.3

# Instalación

prerequisitos

* pip:

  instalamos pip3 metodo get pip

  sudo apt-get install curl

  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

  sudo python3 get-pip.py

* virtualenv (opcional):

  Instalar virtualenv

  sudo apt-get install python-virtualenv virtualenv

  Comando para ver ruta de nuestro interprete python:

  which python3

  Comando para crear entorno virtual:

  virtualenv nombre_de_mi_entorno -p /usr/bin/python3

  Comando para activar el entorno:

  source nombre_de_mi_entorno/bin/activate

  Comando para desactivar el entorno:

  deactivate

1.Clonar repositorio.

    

2.Entrar a la carpeta coreex.

    cd coreex

3. Instalar dependencias con pip. (Si estas usando entorno virtual recuerda activarlo)

    pip install -r requirements/local.txt

4.Realizar las migraciones

    python manage.py makemigrations

    o hacer las migraciones por separado en caso de que no falle el comando 

    python manage.py makemigrations configuration
    python manage.py makemigrations website

    y por ultimo crear la base de datos

    python manage.py migrate

5.Cargar data inicial:


6.Correr el proyecto:

    python manage.py runserver

Datos de pruebas:

  ./manage.py loaddata django_modules/modules/configuration/data/user.json

- Usuario administrador

    Username: admin
    Password: admin

- Usuario de pruebas

    Username: user_test@gmail.com
    Password: coreex123456

