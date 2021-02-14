# Geoloc API
this is a technical task to build a simple API that requires JWT auth and stores geolocation data based on IP or URL

the project is avaliable at https://geoloc-api.herokuapp.com/api/list

## Technologies
* Python 3.9
* Django 3.1.6
* Django Rest Framework 3.12.2

## Setup
To run this project you have to have Python 3.9 installed locally, create a virtual environment and run command

```pip install -r requirements.txt```

After the required packages are installed use commands

```
python manage.py migrate
python manage.py loaddata sample_data.json
python manage.py runserver
``` 

The development server should start and the app should be accessible at [localhost:8000]


## URLs

List of all stored data: 'api/list/'

Detailed info of one IP: 'api/<ip>/'

Retrieve JWT token: 'jwt/token/'

Refresh JWT token: 'jwt/token/refresh/'


## Credentials

The credentials for retrieving JWT token are:
Username: admin
Password: admin
