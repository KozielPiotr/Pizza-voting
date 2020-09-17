
# Table of Contents
* [Overview](#overview)
* [Installation](#installation)
* [Setup](#setup)
* [Endpoints](#endpoints)
  * [pizzas/](#pizzas)
  * [toppings/](#toppings)
  * [votes/](#votes)
  

# Overview
**Pizza voting** is a backend REST application written in **Python**.  
The purpouse of this app is allowing users to cast votes on their favourite compositions of pizza toppings. Users can create their own compositions, as well as toppings.
Instead of voting for specific pizza, user creates own composition of toppings. If that composition already exists, it gains +1 vote. If not, new composition with one vote is created.  
The application allows to track the popularity of individual toppings, not just entire compositions.

<a name="installation"><a/>
  
# Installation

## Prerequisites
- Main:
  - [Python](https://www.python.org/) version 3.8
  - [Django](https://www.djangoproject.com/) version 3.1.1
  - [Django REST framework](https://www.django-rest-framework.org/) version 3.11.1
- Developement:
  - [Pylint](https://www.pylint.org/) version 2.6.0
  - [Black](https://github.com/psf/black) version 20.8b1
  
## Setup Environment Variables
Set the ```SECRET_KEY``` environment variable:
### Linux
```bash
export SECRET_KEY="your_secret_key_here"
```

### Windows
```bash
set SECRET_KEY="your_secret_key_here"
```

## Install required packages
Remember to work in virtual environment.
### main requirements
```bash
pip install -r requirements.txt
```
### dev requirements
In developement I use Black. With some pip managers (as Pipenv) you have to add *--pre* flag, as Black doesn't have official 1.0 release
```bash
pip install -r requirements-dev.txt
```

## Make database migration
Change directory to *pizza_voting*:
```bash
cd pizza_voting
```
Make migrations:
```bash
python manage.py migrate
```

<a name="setup"><a/>

# Setup

## Run application
```bash
python manage.py runserver
```
If you run the application locally, by default it is accessible at **http://127.0.0.1:8000/**

## Prepopulate database
To instantly see all app funcionalities you can prepopulate the database with some data:
```bash
python manage.py prepopulate_db
```

<a name="endpoints"><a/>

# Endpoints

## pizzas/
**pizzas/** endpoint returns list of all pizzas compositions.

### fields
* *url*: URL to detailed view of single pizza object;
* *toppings*: topping objects related to pizza represented by list of toppins names;
* *votes_count*: an amount of votes casted for the pizza composition.

Example:
```json
[
    {
        "url": "http://127.0.0.1:8000/pizzas/1/",
        "toppings": [
            "ham",
            "broccoli"
        ],
        "votes_count": 5
    },
    {
        "url": "http://127.0.0.1:8000/pizzas/3/",
        "toppings": [
            "oregano",
            "mushrooms"
        ],
        "votes_count": 3
    }
]
```

### methods
* *GET*: creates above view of the pizzas list.

POST is not allowed due to method of *pizza* object construction It is created with a *vote* object.

## pizzas/\<pk\>
**pizzas/\<pk\>** endpoint returns detailed view of *pizza* object.
  
### fields
* *url*: URL to detailed view of single pizza object;
* *toppings*: topping objects related to pizza represented by list of toppins names;
* *votes_count*: an amount of votes casted for the pizza composition.

Example:
```json
{
    "url": "http://127.0.0.1:8000/pizzas/1/",
    "toppings": [
        "ham",
        "broccoli"
    ],
    "votes_count": 5
}
```

### methods
* *GET* returns above view of the pizzas list;

PUT and PATCH are not allowed due to method of *pizza* object construction It is created with a *vote* object and should not be editable. Editing pizza's topping would result in creation of the new composition, which is made through creating new *vote*.
Lack of authentication causes also (besided above) not allowing DELETE method.

## toppings/
**toppings/** endpoint returns list of all *topping* objects.

### fields
* *votes_count*: an amount of votes for compositions, where this topping is present;
* *name*: name of the topping.

Example:
```json
[
    {
        "votes_count": 5,
        "name": "oregano"
    },
    {
        "votes_count": 9,
        "name": "ham"
    },
    {
        "votes_count": 4,
        "name": "spinach"
    }
]
```

### methods
* *GET* returns above view of the toppings list;
* *POST* creates new *topping* object. Accepts only "name" field as a string.
  
There is no detailed view of this endpoint. Existing toppings should not be changed or deleted. Lack of this mechanism is caused by a lack of any authentication system.

## votes/
**votes/** endpoint returns list of all *votes* objects.

### fields
* *timestamp*: time of the *vote* creation;
* *pizza*: URL to detailed view of the related *pizza* object;
* *toppings*: **write only**, multiple choice field with toppings names.

Example:
```json
[
    {
        "timestamp": "2020-09-17T07:55:10.256860Z",
        "pizza": "http://localhost:8000/pizzas/6/"
    },
    {
        "timestamp": "2020-09-15T22:32:49.864449Z",
        "pizza": "http://localhost:8000/pizzas/5/"
    },
    {
        "timestamp": "2020-09-15T22:32:49.722441Z",
        "pizza": "http://localhost:8000/pizzas/5/"
    }
]
```

### methods
* *GET* returns above view of the votes list;
* *POST* creates new *vote* object. Accepts only *toppings* field with list of toppings represented by their names as strings. Chosen toppings combination is searched through existing *pizza* objects. If found, new *vote* is related to it. If not, beside of the nev *vote*, new *pizza* object is created and related to new *vote*.

Due to creation method this endpoint doesn't have a detailed view. Also, *votes* can not be deleted due to the lack of any authentication system.
