# JSON format (like a server-client connection)

template = '''
{
    "results": [
        {
            "name": "Xenoner",
            "points": 12
        },
        {
            "name": "Vasutin",
            "points": 123
        }
    ]
}
'''

import json

with open("path/to/save/data.json", 'r') as f:
    loaded = json.load(f)

loaded['results'].append({'name': 'Blokhin', 'points': 312})

with open("path/to/save/data.json", 'w') as f:
    json.dump(loaded, f)


# YAML format: simpler than JSON (may be)

template = '''
results:
  - name: Vasutin
    points: 12
  - name: Nazarchuk
    points: 13
count_games: 12
'''

import yaml

with open("path/to/save/data.yaml", 'r') as f:
    loaded = yaml.load(f)

loaded['results'].append({'name': "Kim", 'points': 32})
    
with open("path/to/save/data.yaml", 'w') as f:
    yaml.dump(loaded, f)


# Save raw python objects (with methods and etc.)

import pickle

data = [(1, 2, 3) for _ in range(4)]

with open("path/to/save/data.pickle", 'wb') as f:
    pickle.dump(data, f)

with open("path/to/save/data.pickle", 'rb') as f:
    load_new = pickle.load(f)
