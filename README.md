# Rest-API
Django Rest API Application
 
This is a rest api application I made using the django framework. This application supports POST, PUT, GET, and DELETE commands on any arbitrary JSON object. This means that all the JSON objects can have any number of fields and different fields. Also, each JSON object is assigned a unique identifier.

This application is uploaded to Heroku and can be accessed at this link: https://eaglerestapi.herokuapp.com/api/objects.

Note that when making commands, there may be some lag time, so keep refreshing if you don't see any updates or it returns an error that shouldn't be thrown after doing a command. 

If running locally, make sure python3 is downloaded. Then download django and djangorestframework using pip.

```bash 
$ pip install django
#
$ pip install djangorestframework 
#
```
Download the restapi project folder here and then using terminal move into the folder. Run these commands now in local directory.

```bash 
$ python3 manage.py makemigrations
#
$ python3 manage.py migrate
#
$ python3 manage.py runserver
#
```

The application should now be available at http://127.0.0.1:8000/api/objects.

POST to api/objects : Input any number of arbitrary fields in JSON format, and the response is the JSON object with all the inputted fields with a unique identifier field for the posted object.

PUT to api/objects/&lt;uid> : Input any number of arbitrary fields in JSON format, and the response is the JSON object with all the inputted fields with the unique identifier field as the uid in the url.
  
GET to api/objects/&lt;uid> : Response of the JSON object with the uid specified with all its fields.
  
GET to api/objects : Response of all the urls of the JSON objects in JSON format.

DELETE to api/objects/&lt;uid> : No response, and deletes the JSON object with the uid unique identifier.
  
Errors : There are scenarios where errors are returned as response. Some errors include posting or putting something not in JSON format or getting, putting, or deleting a nonexistant JSON object.
