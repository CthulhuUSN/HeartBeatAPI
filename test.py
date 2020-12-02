import json

data = {}
data2 = {}
data['key'] = 'value'
data['key2'] = 'value2'
data2['key3'] = 'value3'
data2['key4'] = 'value4'
data['key5'] = data2
json_data = json.dumps(data)

print(json_data)