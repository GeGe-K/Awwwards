# Awwwards

## Author
### *Gloria Givondo* (21/12/2018)

## Description
An application which allows a user to post a project he/she has created and get it reviewed by his/her peers.

You can view the live link [here]()

## User Stories
These are the behaviours that the application implenents for use by a user.

As a user, I would like to: 
* View posted projects and their details.
* Post a project to be rated/reviewed.
* Rate/ review other users' projects.
* Search for projects. 
* View projects overall score.
* View my profile page.

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Django
* Python version 3.6

### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/GeGe-K/Awwwards.git
        $ cd Awwwards

* Activate virtual environment

        $ source virtual/bin/activate

* Download the latest version of pip

        $ curl https:/bootstrap.pypa.io/get-pip.py | python

* Install application dependancies and other Modules

        $ pip install -r requirements.txt

* Create the database

        $ psql
        
        CREATE DATABASE awards;

* Create a .env file and add the following

        - SECRET_KEY = `<secret_key>`
        - DB_NAME = `awards`
        - DB_USER = `<Username>`
        - DB_PASSWORD = `your db password`
        - DEBUG = `True`

* Run initial migration

        $ python3.6 manage.py makemigrations <name of app>
        $ python3.6 manage.py migrate

* Run the application in your terminal:

        $ python3.6 manage.py runserver

### Django Admin
* Username: moringaschool 
* Password: <see_me>

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Technologies Used
* Virtual environment
* Python version 3.6.7(Django framework)
* Bootstrap4
* Postgresql
* HTML5
* CSS
* Heroku
* Visual Studio Editor

## Known Bugs
There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**