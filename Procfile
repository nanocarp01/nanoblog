release: python manage.py migrate
web: gunicorn blog.wsgi:application --bind 0.0.0.0:$PORT

