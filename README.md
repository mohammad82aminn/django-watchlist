# Django Watchlist

A personal movie watchlist built with Django: each movie has a title, release year, rating and a short review.
Built while practicing Models, migrations, the Django Admin, the ORM, templates and tests.

## Tech stack

- Python 3.12
- Django 6.1
- SQLite

## Run locally (Windows cmd)

```bat
git clone https://github.com/<your-username>/django-watchlist.git
cd django-watchlist
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
```

Put a real secret key in `.env`, then:

```bat
python manage.py migrate
python manage.py runserver
```

## Run tests

```bat
python manage.py test
```