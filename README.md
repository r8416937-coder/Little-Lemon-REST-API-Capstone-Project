# Little Lemon REST API Capstone Project

This submission contains the required Django project `littlelemon` and the required app `restaurant`.

## Grading checklist

- Project folder is named `littlelemon`.
- App folder is named `restaurant`.
- `restaurant`, `rest_framework`, `rest_framework.authtoken`, and `djoser` are included in `INSTALLED_APPS`.
- `TEMPLATES['DIRS']` points to the `templates` folder.
- `templates/index.html` exists and is connected to the home view.
- MySQL is configured in the `DATABASES` section of `settings.py`.
- `models.py` contains `Menu` and `Booking` models.
- `admin.py` registers `Menu` and `Booking`.
- `serializers.py` contains serializer classes for `Menu` and `Booking`.
- `views.py` contains `MenuViewSet` and `BookingViewSet`.
- `restaurant/urls.py` contains the API routes and the `api-token-auth/` route using `obtain_auth_token`.
- `littlelemon/urls.py` contains Djoser endpoints through `auth/` and browsable API login through `api-auth/`.
- `test_models.py` and `test_views.py` contain unit tests.
- `insomnia_collection.json` is included so the endpoints can be tested in Insomnia.

## Main endpoints

- `/` home page
- `/api/menu-items/`
- `/api/menu-items/<id>/`
- `/api/bookings/`
- `/api/bookings/<id>/`
- `/api-token-auth/`
- `/auth/users/`
- `/auth/token/login/`
- `/auth/token/logout/`
- `/api-auth/`
- `/admin/`

## Run the project

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Test with Insomnia

Import `insomnia_collection.json`, then test:

1. `GET /api/menu-items/`
2. `POST /api/menu-items/`
3. `GET /api/bookings/`
4. `POST /api/bookings/`
5. `POST /api-token-auth/`
6. Djoser endpoints under `/auth/`
