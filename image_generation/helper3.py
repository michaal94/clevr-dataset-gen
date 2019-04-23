import os
import json

path = '../question_generation/metadata.json'

with open(path, 'r') as f:
    metadata = json.load(f)

classes = dict()
i = 0
for attr in ['Size', 'Weight', 'Color', 'Material', 'Movability', 'Shape', 'Name']:
    for val in metadata['types'][attr]:
        if attr == 'Material' and val == 'glass':
            val = 'glass_material'
        classes[val] = i
        i += 1

with open('./attr_idx.json', 'w') as f:
    json.dump(classes, f, indent=4, separators=(',', ': '))

