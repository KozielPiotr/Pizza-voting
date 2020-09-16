# Table of Contents
* [Overview](#overview)
* [Installation](#installation)
* [Setup](#setup)

# Overview
**Pizza voting** is a backend REST application written in **Python**.  
The purpouse of thiss app is allowing users to cast votes on their favourite compositions of pizza toppings. Users can create their own compositions, as well as toppings.

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
