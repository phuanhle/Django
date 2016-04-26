#from django.shortcuts import render
#from django.template import loader
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
import json
from bson import json_util
from django.utils import html
from MyDjangoApp.models import MySampleModel
from config import getConfig



#This is Django try to read data from MongoDB cannot use data model in models.py
#using default port and host=localhost if using different the specify in arguments

config = getConfig()
print "Connect to DB:" + config["db"]

client = MongoClient(host=config["host"],port = config["port"])
db = client[config["db"]]


#return render_to_response('html/index.html')
#return HttpResponse(template.render(request))
#result = db.mytable.find({ "$or" : [{'Age': '35'} , {'Age': '45' }]  } )
#result = db.mytable.find({ "$or" : [{'Age': '35'} , {'Age': '45' }]  } )    
#result = MySampleModel(title = 'test title',  text = 'test content')  



def json_format(obj):
    json_docs = []    
    for doc in obj:
        json_doc = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)                
        json_docs.append(json.loads(json_doc))    
    return json_docs

#using http POST
def search(request):
    #response = HttpResponse()
    exp = request.POST.get("Age", '')    
    if exp == "*":
        result = db.mytable.find()
    else:
        result = db.mytable.find({"Age" : exp} )                        
    #return JsonResponse(json.dumps(json_format(result)), safe=False)
    return JsonResponse(json_format(result), safe=False)
    



#Using RESful
def detail(request, question_id):            
    if(question_id == "*"):
        result = db.mytable.find()
    else:
        result = db.mytable.find({ "Age": question_id } )
        
    ##data = MySampleModel(name = 'Hanh',  age = '30', street='SSS')
    ##data.save()
    #data = MySampleModel()
    #it = data.objects.all()
    #print MySampleModel.objects.get(name='Hanh')
    return JsonResponse(json_format(result), safe=False)
    

    
# Unable to configure this to work with DATABASES = { 'ENGINE': 'django_mongodb_engine' }  
#data = MySampleModel("Hanh", "45", "1234")  
#print data
#data.save() #this save to SQLite

#Update the record
#db.mycol.update({'title':'MongoDB Overview'},{$set:{'title':'New MongoDB Tutorial'}})
def update(request):
    age = request.POST.get('Age', '')
    name = request.POST.get('Name', '')
    street = request.POST.get('Street', '')            
    ret = db.mytable.update(
        { "Age": age }, 
        {
            "Age" : age,
            "Name": name,
            "Street" : street
        }
    )    
    return JsonResponse(json.dumps(ret), safe=False)

#Insert new record    
def insert(request):
    age = request.POST.get('Age', '')
    name = request.POST.get('Name', '')
    street = request.POST.get('Street', '')            
    ret = db.mytable.insert( 
        {
            "Age" : age,
            "Name": name,
            "Street" : street
        }
    )        
    return JsonResponse(json.dumps(ret), safe=False)

#Delete one record
def delete(request):
    age = request.POST.get('Age', '')
    name = request.POST.get('Name', '')
    street = request.POST.get('Street', '')                
    ret = db.mytable.remove({"$and" : [{'Age': age }, {'Name': name }, {'Street': street }]   })        
    return JsonResponse(json.dumps(ret), safe=False)

# Create your views here.
