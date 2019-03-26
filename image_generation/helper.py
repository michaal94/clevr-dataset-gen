import os

shapes_list = sorted(os.listdir('./data/shapes'))
for i in reversed(range(len(shapes_list))):
    if '.blend' not in shapes_list[i]:
        shapes_list.pop(i)

objects = dict()

for i in range(len(shapes_list)):
    text = "obj%02d" % (i + 1)
    obj = shapes_list[i].split('.')[0]
    objects[text] = obj

print(objects)

import json

with open('./objects.json', 'w') as f:
    json.dump(objects, f, sort_keys=True, indent=4, separators=(',', ': '))

