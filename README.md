# Graphene-sqlalchemy
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This example project demos integration between Graphene, Flask and SQLAlchemy.he project contains two models, one named Classes and another named Students.
	
## Technologies
Project is created with:
* Flask
* Graphen
* SQLAlchemy
	
## Setup
First you'll need to get the source of the project. Do this by cloning the whole Graphene-SQLAlchemy repository. We'll do this using virtualenv to keep things simple, but you may also find something like virtualenvwrapper to be useful.

Create a virtualenv in which we can install the dependencies:
```
virtualenv env
source env/bin/activate
```
Now we can install our dependencies:
```
pip install -r requirements.txt
```
Now the following command will setup the database, and start the server:
```
 ./app.py
```
Now head on over to http://127.0.0.1:5000/graphql and run some queries!
