
# Space API

Space API is a REST API made with django rest framework which allows to get information about objects like: planets, planetary systems, galaxies, rockets, space missions \
Also It has a simple frontend to test the application made with React.

Rest API that returns data to objects such as:
- planets, 
- planetary systems,
- galaxies,
- rockets 
- space missions. 
By providing an email address, the user can receive a token, which can then be used for authorization. \
In addition, it has a frontend made in React.


## Demo

<img src="/images/demo.gif"/>

- [YOUTUBE LINK](https://www.github.com/DEENUU1) [IN PROGRESS]


## The project is divided into 2 sections:

### Rest API made in Django Rest Framework.
There is 5 models: Planet, Galaxy, System, Rocket and Mission and endpoints for them are:

<img src="/images/endpoint_1.png"/>

<img src="/images/endpoint_2.png"/>


#### GET /api/planets
Allows to display a list of planets with pagination which display 10 objects on 1 page 
#### GET /api/systems 
Allows to display a list of planetary systems with pagination which display 10 objects on 1 page 
#### GET /api/galaxies 
Allows to display a list of galaxies with pagination which display 10 objects on 1 page 
#### GET /api/galaxies/<galaxy_id>/systems/
#### GET /api/system/<galaxy_id>/planets/
#### GET /api/system/<system_id>/panets/
#### GET /api/planet/<id>
#### GET /api/system/<id>
#### GET /api/galaxy/<id>
#### GET /api/rockets -> Allows to display a list of rockets with pagination which display 10 objects on 1 page 
#### POST /api/rocket/create
#### GET /api/missions 
Allows to display a list of missions with pagination which display 10 objects on 1 page 
#### POST /api/mission/create 


### Frontend using React
To be honest this is my first time using React, I only know a little bit of JavaScript but I did a few pages and hooks which allows to display data from few endpoints and create/delete user's token.


### Project is based on technologies such as:
- Python (Django, Django Rest Framework)
- React 

## Installation

Clone the repository

```bash
git clone <link>
```

Install the requirements

```bash
pip install -r requirements.txt
```

Inside spcae_api folder add .env file. It should looks like this:

```bash
SECRET_KEY=XXXXXXXX
EMAIL_HOST_USER=XXXXXXXX
EMAIL_HOST_PASSWORD=XXXXXXXX
```

Now run Django server using this command 

```bash
py manage.py runserver
```

And then you can run React app

Go to frontend folder

```bash
cd frontend
```

And then run the node server

```bash
npm start
```
## Running Tests

To run tests, run the following command

```bash
  py manage.py test <APP NAME>.tests 
```

For example to run tests for "base" application you can type: 

```bash
py manage.py test base.tests
```


## Authors

- [@DEENUU1](https://www.github.com/DEENUU1)

