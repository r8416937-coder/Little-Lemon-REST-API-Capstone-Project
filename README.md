# Little Lemon REST API

Django REST Framework API for Little Lemon restaurant menu items, table bookings, registration/authentication with Djoser and token auth, MySQL database configuration, templates, and unit tests.

## Required project names
- Project: `littlelemon`
- App: `restaurant`

## Endpoints
- `/` home page using `templates/index.html`
- `/api/menu-items/`
- `/api/bookings/`
- `/api-token-auth/`
- `/auth/` Djoser endpoints
- `/admin/`

## Run
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
