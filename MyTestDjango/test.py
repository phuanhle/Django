import json
from bson import json_util


file = open('data.json', 'r')
#while True:
#    line = file.read()
#    print line
#    if not line: break
file.close()


#with open('data.json', 'w') as f:
#     json.dump(data, f)
     
     
with open('data.json', 'r') as f:
    data = json.load(f)
    print data['price'] 
    json_str = json.dumps(data)
    print json_str
    f.close()

