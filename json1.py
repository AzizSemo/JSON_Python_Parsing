import json

with open('JSON_Sample.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(type(data))
#print(data.keys())
#print(data.values())
print("Name\t\t Job\t\t Email")
for x in data.values():
    for y in x:
       print(str(y["firstName"]) +"\t\t"+ str(y["jobTitle"])+"\t\t"+ str(y["emailAddress"]) )
        
