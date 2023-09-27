Comando para borrar migraciones

Advertencia: este comando es peligroso, asegurate se respaldar

situate en la rais del proyecto y ejecuta:

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

Comando para extraer datos en formato json

./manage.py dumpdata --exclude auth.permission --exclude contenttypes location.country > country.json

./manage.py loaddata country.json








