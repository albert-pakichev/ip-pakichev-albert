import json
data = {'name': 'Vasiliy',
        'surname': 'Petrov',
        'address': {'sity': 'HOLLYWOOD', 'street': 'New'}\
        }
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('data.json', 'r') as f:
    data2 = json.loads(f.read())
