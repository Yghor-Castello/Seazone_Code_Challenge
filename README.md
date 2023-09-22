# READ ME

# Seazone Code Challenge - APIs Backend Vacancy Python Developer

This is a project developed with Python and Django Rest Framework. This project includes three main apps:

1. **Royalty** - Handles property information.
2. **Advertisement** - Deals with property listings on various platforms.
3. **Reservation** - Manages reservations made on these property listings.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup using Docker](#setup-using-docker)
- [Local Setup](#local-setup)
- [Loading Initial Data](#loading-initial-data)
- [Apps Context](#apps-context)

## Prerequisites

- Python 3.8 or higher
- Docker & Docker-Compose (if you're using the Docker setup)

## Setup using Docker

1. Clone the repository:
    ```
    git clone https://github.com/Yghor-Castello/Seazone_Code_Challenge.git
    ```

2. Navigate to the project directory:
    ```
    cd Seazone_Code_Challenge
    ```

3. Build and run the Docker containers:
    ```
    docker-compose up --build
    ```

4. Create migrations for the project:
    ```
    docker-compose exec backend python manage.py makemigrations
    ```

5. Apply the migrations:
    ```
    docker-compose exec backend python manage.py migrate
    ```

6. Create a superuser for the Django admin:
    ```
    docker-compose exec backend python manage.py createsuperuser
    ```

The system should now be running at `http://localhost:8000/`.

## Local Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Yghor-Castello/Seazone_Code_Challenge.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Seazone_Code_Challenge
    ```

3. Set up a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Create migrations for the project:
    ```bash
    python manage.py makemigrations
    ```

5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

The system should now be running at `http://localhost:8000/`.

## Loading Initial Data

The project includes fixtures to help populate the database with initial data.

To load this data into the database, run:

1. python manage.py loaddata core/fixture/fixture_realty.json
2. python manage.py loaddata core/fixture/fixture_advertisement.json
3. python manage.py loaddata core/fixture/fixture_reservation.json

## Testing

To run specific test cases, use the following commands:

```bash
1. python manage.py test core.tests.tests_realty.RealtyViewTestCase
2. python manage.py test core.tests.tests_advertisement.AdvertisementViewTestCase
3. python manage.py test core.tests.tests_reservation.ReservationViewTestCase
```

## API Endpoints Documentation

The available endpoints in the API can be viewed using the following documentation tools:

- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [ReDoc](http://127.0.0.1:8000/redoc/)

