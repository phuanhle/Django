#from django.shortcuts import render
#from django.template import loader
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
import json
from bson import json_util
from django.utils import html
from config import getConfig
import logging
from django.http import QueryDict

#HTTP Status Codes
#200's are used for successful requests. 
#300's are for redirections. 
#400's are used if there was a problem with the request. 
#500's are used if there was a problem with the server.


#This is Django try to read data from MongoDB cannot use data model in models.py
#using default port and host=localhost if using different the specify in arguments

config = getConfig()
logging.basicConfig(filename=config["logfile"],level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
logging.info("Connect to DB:" + config["db"])

client = MongoClient(host=config["host"],port = config["port"])
db = client[config["db"]]


def json_format(obj):
    json_docs = []    
    #if type(obj) is list:    
    for doc in obj:
        json_doc = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)                
        json_docs.append(json.loads(json_doc))
    return json_docs

#GET
def search(request, json_query):
    #print json_query        
    logging.info("search/"+json_query)
    ret = db.mytable.find( json.loads(json_query))
    return JsonResponse(json_format(ret), safe=False)

  
#POST  
def insert(request):
    data = request.POST.get("myarea", '')     
    logging.info("insert/"+data) 
    ret = db.mytable.insert(json.loads(data)) 
    #return JsonResponse(json_format(ret), safe=False)
    return HttpResponse(json.dumps(ret, default=json_util.default), content_type="application/json")

#PUT
def update(request, json_query):
    #mydata = QueryDict(request.body)
    #json_query = mydata['myarea']
    logging.info("update/"+json_query)
    myinput = "[" + json_query + "]"
    myjson = json.loads(myinput)    
    ret = db.mytable.update(myjson[0],myjson[1])
    return HttpResponse(json.dumps(ret, default=json_util.default), content_type="application/json")    


#DELETE
def delete(request,json_query):    
    logging.info("delete/"+json_query)
    ret = db.mytable.remove(json.loads(json_query))          
    return HttpResponse(json.dumps(ret, default=json_util.default), content_type="application/json")    
    
    #mydata = QueryDict(request.body)
    #json_query = mydata['myarea']
    #logging.info("delete/"+json_query)    
    #myjson = json.loads(myinput)    
    #ret = {"age":30}  #db.mytable.update(myjson[0],myjson[1])
    #return HttpResponse(json.dumps(ret, default=json_util.default), content_type="application/json")    


# Create your views here.
