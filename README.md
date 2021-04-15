# microblog-backend

This is the backend API for our demo microblog (knockoff twitter) application.

It is written in Python using the [Django](https://www.djangoproject.com/) framework.

---

## How to run it

### Install requirements

* Python3
* pipenv - Install with `pip install pipenv`

Install dependencies with `pipenv install`

### Run a local server

`python manage.py runserver`

### Perform database migration

`python manage.py migrate`

### Run production server

`gunicorn config.wsgi -b 0.0.0.0:8000`

### Creating an admin user

`python manage.py createsuperuser`
Then follow the prompt

### Accessing the admin panel

Access `http://{your_host}:8000/admin`

User your superuser account to login

---

## Necessary configuration

| Environment variable | Options/Type | Default | Description |
| --- | --- | --- | --- |
| DEBUG | True/False | True | Enables or disables Django debug mode |
| DB_NAME | String | postgres | Database name |
| DB_USER | String | postgres | Database user's name |
| DB_PASS | String | postgres | Database user's password |
| DB_PORT | String | postgres | Database port number |

## Deploying with Helm

In order to deploy this application with Helm you'll need to update a few fields either with a custom values.yaml file or passed in on the cli.

### Example deploy

You'll need to update all of these fields with your own values.

```shell
helm upgrade --install microblog-backend ./chart \
  --set hostname=backend.example.com \
  --set image.repository=gcr.io/my_registry/backend \
  --set image.tag=asd9f8
```
