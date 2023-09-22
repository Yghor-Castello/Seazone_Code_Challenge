# Seazone Code Challenge - APIs Backend Vacancy Python Developer

This is a project developed with Python and Django Rest Framework. The goal of this project is to provide a REST API for a wedding company.

# Criação de Ambiente Virtual WSL

Criando Ambiente virtual: 
    - virtualenv venv

Ativando Ambiente virtual:
    - source venv/bin/activate

## Installation

Before starting, it is recommended to check if you have docker and docker compose installed on the machine, if not, check how to install according to your operating system.

## Execution

Start application.

``` wsl
1 - docker-compose up --build
2 - Open a new wsl terminal
3 - docker-compose exec backend python manage.py makemigrations
4 - docker-compose exec backend python manage.py migrate
5 - docker-compose exec backend python manage.py createsuperuser
```

```fixture
1 - python manage.py loaddata core/fixture/fixture_realty.json
2 - python manage.py loaddata core/fixture/fixture_advertisement.json
3 - python manage.py loaddata core/fixture/fixture_reservation.json
```

```tests
1 - python manage.py test core.tests.tests_realty.RealtyViewTestCase
2 - python manage.py test core.tests.tests_advertisement.AdvertisementViewTestCase
3 - python manage.py test core.tests.tests_reservation.ReservationViewTestCase
```

## Endpoints

Endpoints available in the API can be viewed by swagger
[http://127.0.0.1:8000/swagger/]
[http://127.0.0.1:8000/redoc/]