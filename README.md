# How to run locally

- virtualenv -p python3 env_pm
- activate the new environment (source env_pm/bin/activate)
- clone from Github
- python manage.py makemigrations portal_app
- python manage.py migrate
- python manage.py runserver
