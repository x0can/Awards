# The Gram

>[Alex-MWaura](https://awards21.herokuapp.com/)  
  
# Description  
This is a clone of  Instagram where people share their  images for other users to view. 
Users can sign up, login, view and post photos and search  other users.
##  Live Link  
 Click [View Site](https://awards21.herokuapp.com/)  to visit the site
  
 
## User Story  
  
* Click on icon to sign in or Register  
* Upload a project with some of its secreen shots.
* Update profile 
* View Api Endpoint
* Search for different projects using projects title.  
* Hover over image to vote or view project posted


  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd The-Gram pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations Awards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.7](https://www.python.org/)  
* [Django 1.11.17](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [alexmwaura43@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)]()  
* Copyright (c) 2019 **Alex Mwaura**