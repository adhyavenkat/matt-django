# news-app

## virtual environment

# Creates a virtual environment

python3 -m venv env

# Activate the virtual environment

source env/bin/activate


## Dependency Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

pip install -r requirements.txt


## DB Configurations

# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_schema_name',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

## Migrations

python manage.py makemigrations

python manage.py migrate

## To create admin user

python manage.py createsuperuser

## To run server

python manage.py runserver

## Run Docker compose 

docker-compose up -d

## To remove the container

docker-compose down -v

## Endpoints
## To get all news

http://127.0.0.1:8011/api/v1/news/?page=1&page_size=1

# To get news by category id

http://127.0.0.1:8011/api/v1/news/?category_id=1

# To get all active categories(ascending by name)

http://127.0.0.1:8011/api/v1/category/



