Debian 10 64bit trabajar con python3.7

Asi debian venga con python3 instalado se de instalar python3-setuptools

sudo apt-get install python3-setuptools

instalamos pip3 metodo get pip

sudo apt-get install curl

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

sudo apt-get install python3-distutils

sudo python3 get-pip.py



Instalar virtualenv

sudo apt-get install virtualenv

which python3

virtualenv env-crawler -p /usr/bin/python3



Comandos:

Eliminar todos los pyc de cualquier proyecto:

find . -name \*.pyc -delete

Eliminar todos los pycache:

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf



Instalar spyder3 editor

sudo apt-get install spyder3



En caso de usar python con postgres instalar conector:

sudo apt-get install libpq-dev python-dev

sudo apt-get install python3-psycopg2

sudo apt-get install python3-dev


