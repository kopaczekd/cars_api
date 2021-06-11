# CARS API

## Project launch
To run this project on your computer You have two ways:
  
### DOCKER
If You have a docker on your machine:
- download whole repository, 
- open terminal and enter to folder which contains docker-compose.yml file,
- make sure that you have free port on localhost,
- run this command "docker-compose up"

### RUNSERVER
You can also start this project without docker. Make sure that You have installed on your local machine:
- python3
- pipenv  

Then download whole repository and open terminal enter to folder which contains Pipfile and create your local environment:
- pipenv install  
- pipenv shell

Then enter to folder which contains manage.py file and run:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


## Functionalities

All functionalities we can seperate for few endpoints:

### Application Cars

#### Method POST - /cars/

- Request body contains car make and model name
- Based on this data, its existence is checking here https://vpic.nhtsa.dot.gov/api/
- If the car doesn't exist - returning an error
- If the car exists - is saving in the database

```json
{
  "make" : "Volkswagen",
  "model" : "Golf"
}
```

#### Method GET - /cars/

- Fetching a list of all cars already present in application database with their current average rate

```json
[
    {
      "id" : 1,
      "make" : "Volkswagen",
      "model" : "Golf",
      "avg_rating" : 5.0
    },
    {
      "id" : 2,
      "make" : "Volkswagen",
      "model" : "Passat",
      "avg_rating" : 4.7
    }
]

```

#### Method DELETE - /cars/{id}

- Deleting the car with the given id from database
- If the car doesn't exist in database - returning an error

### Application Rate

#### Method POST - /rate/

- Adding rate for car from 1 to 

```json
{
  "car_id" : 1,
  "rating" : 5
}
```
  
### Application Popular
- Returning top cars already present in the database ranking based on a number of rates

```json
[
    {
      "id" : 1,
      "make" : "Volkswagen",
      "model" : "Golf",
      "rates_number" : 100
    },
    {
      "id" : 2,
      "make" : "Volkswagen",
      "model" : "Passat",
      "rates_number" : 31
    }
]

```

## Extra info

All three endpoints have their own tests.  
Online version of this project will be available soon!
