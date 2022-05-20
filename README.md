# Squadmakers Backend Dev Test

# Run locally

### Create a locally database in postgres

### Install python 3

### Install requirements

`pip install -r requirements.txt`

### Migrate

`python manage.py migrate`

### Collectstatics

`python manage.py collectstatic --no-input`

### Execute tests

`pytest`

### Run

`python manage.py runserver`

# Run With Docker

### Start the project

Configure your .env as the example and run `docker-compose up`

### Execute tests

After build, run tests `docker-compose run --rm test`

# DOCS

### Swagger YAML collection

File: swagger.yaml

[Docs](http://127.0.0.1:8000/)

## Other questions

The second part of the questions in the file questions.md

