import json
"""
with open("interfaces.json") as f:
    ori_data = f.read()
    
interfaces = json.loads(ori_data)
print(interfaces)


data = {"router":{"vendor":"Cisco","interfaces":{"interface":[{"name":{"name":"GigabitEthernet0/0"}},{"name":{"name":"GigabitEthernet0/1"}}],"hostname":{"name":{"name":"R1"}}}}}

data_json = json.dumps(data, indent=4)
print(data_json)
"""

#print(dir(json))

#print(json.__all__)
#print(json.__author__)


data = '111'
print(type(json.loads(data)))
