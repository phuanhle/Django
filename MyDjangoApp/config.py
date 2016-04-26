import json

def getConfig():    
    with open('C:\workspace\MyTestDjango\data.json', 'r') as f:
        data = json.load(f)
        f.close()         
        #json_str = json.dumps(data)        
    return  data

def saveConfig(obj):
    #data = {"host" : "locahost", "port" : 27017 , "db" : "hanhdb"}
    with open('C:\workspace\MyTestDjango\data.json', 'w') as f:
        json.dump(obj, f)
        f.close()
        