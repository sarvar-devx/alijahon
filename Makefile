mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
user:
	python3 manage.py createsuperuser
dumpdata:
	python3 manage.py dumpdata --indent=2 apps.shop.Product > product.json

loaddata:
	python3 manage.py loaddata categories