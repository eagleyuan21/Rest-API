import uuid # this generates the values of the unique id for each json object
import json
from rest_framework.views import APIView # uses the class based api commands
from rest_framework.response import Response # helps return the dictionary data

""" The reason I chose to use python and dictionaries is because of the necessity to tailor 
the arbitrary type of JSON. Python is more suitable compared to the likes of java and c++
"""

arbs = dict() # stores all json objects with the key as the uid
urls = dict() # stores only the url json objects with the key as the uid

# stores the mutable error object
errors = dict({"verb" : "action" , "url" : "link" , "message" : "mess"})

#CONSTANT_URL = "http://127.0.0.1:8000/api/objects"

# if deploying to Heroku, 
CONSTANT_URL = "https://eaglerestapi.herokuapp.com/api/objects"

# this class is entered only with the /api/objects url, specified in urls.py
class arblist(APIView):
    
    # post commands
    def post(self, request, format=None):
        
        if isinstance(request.data,dict): # checks to see if typed json data is actual json object
            posted = request.data # stores the typed json data into a variable
            unique = str(uuid.uuid4()) # generates uid
            posted.update({'uid' : unique}) # adds the uid to the json data
            arbs[unique] = posted # adds the json data to the "all" dictionary
            temp = {'url' : CONSTANT_URL + "/" + unique} # creates the url object 
            urls.update({unique : temp}) # adds the url object to dictionary with uid as key
            return Response(arbs[unique]) # returns the typed json data with uid key
        
        # returns error if json data is not actual json object
        else: 
            errors["verb"] = "POST"
            errors["url"] = CONSTANT_URL
            errors["message"] = "Not a JSON object"
            return Response(errors)
    
    # get commands (without url endpoint)
    def get(self, request):
        return Response(urls.values()) # return the objects' urls
    
# this class is entered only with the /api/objects/ url with uid added   
class arbdetails(APIView):
    
    # get specific uid
    def get(self, request, uid):
        holder = uid # stores uid in variable
        
        if holder in arbs: # checks for if the uid is an already made json object
            posted = arbs[holder] # sets the json object with uid key
            posted.update({'uid' : holder}) # adds the uid to the json data
            return Response(posted) # return the uid key object
        
        # returns error if json data is not actual json object
        else: 
            errors["verb"] = "GET"
            errors["url"] = CONSTANT_URL + "/" + holder
            errors["message"] = "Not a previously made JSON object"
            return Response(errors)

    # put specific uid
    def put(self, request, uid):
        holder = uid # stores uid in variable
        
        if holder in arbs: # checks for if the uid is an already made json object
            
            if isinstance(request.data,dict): # checks to see if typed json data is actual json object
                posted = request.data # stores the typed json data into a variable
                posted.update({'uid' : holder}) # adds the uid to the json data
                arbs[holder] = posted # sets the json object with uid key to typed json data
                return Response(posted) # return the typed json data with uid key
            
            # returns error if json data is not actual json object
            else: 
                errors["verb"] = "PUT"
                errors["url"] = CONSTANT_URL + "/" + holder
                errors["message"] = "Not a JSON object"
                return Response(errors)
        
        # returns error if json data is not actual json object
        else: 
            errors["verb"] = "PUT"
            errors["url"] = CONSTANT_URL + "/" + holder
            errors["message"] = "Not a previously made JSON object"
            return Response(errors)
    
    # delete specific uid
    def delete(self, request, uid):
        holder = uid # stores uid in variable
        
        if holder in arbs: # checks for if the uid is an already made json object
            del arbs[holder] # deletes the json object with uid key
            del urls[holder] # deletes the url object with uid key 
            return Response({}) # return nothing
        
        # returns error if json data is not actual json object
        else: 
            errors["verb"] = "DELETE"
            errors["url"] = CONSTANT_URL + "/" + holder
            errors["message"] = "Not a previously made JSON object"
            return Response(errors)