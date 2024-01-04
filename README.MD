poetry env use "C:\Program Files\Python311\python.exe"
poetry shell
poetry install

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py dumpdata goods.Categories > fixtures/goods/goods.json
python manage.py loaddata fixtures/goods/goods.json
