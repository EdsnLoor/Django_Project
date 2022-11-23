# Library website built in Django 4.0 and Python

# Django project

This website was built using [Dajngo 4.0](https://www.djangoproject.com/), a Python web framework that encourages rapid
development and clean.

## Installation
Follow Dajngo documentation.

## Make migrations

```console
python manage.py makemigrations
```
Migrations are Django’s way of propagating changes you make to your models
## Migrate

```console
python manage.py migrate
```

## Local Development

```console
python manage.py runserver
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without
having to restart the server.

## Super User

```console
python3 manage.py createsuperuser
```

Creates a superuser account (a user who has all permissions). This is useful if you need to create an initial superuser 
account or if you need to programmatically generate superuser accounts for your site(s).

