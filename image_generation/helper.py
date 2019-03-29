import os
import json

shapes_list = sorted(os.listdir('./data/shapes'))
for i in reversed(range(len(shapes_list))):
    if '.blend' not in shapes_list[i]:
        shapes_list.pop(i)

objects = dict()

for i in range(len(shapes_list)):
    # text = "obj%02d" % (i + 1)
    obj = shapes_list[i].split('.')[0]
    obj_name = ''.join(c for c in obj if not c.isdigit())
    obj_name = ''.join(c if c != '_' else ' ' for c in obj_name)
    obj_change_mat = False
    obj_change_size = False
    obj_material = 'FILL'
    obj_color = 'FILL'
    obj_size = 'FILL'
    objects[obj] = {
        'name': obj_name,
        'change_material': obj_change_mat,
        'change_size': obj_change_size,
        'material': obj_material,
        'color': obj_color,
        'size': obj_size
    }

print(objects)


with open('./object_properties.json', 'w') as f:
    json.dump(objects, f, sort_keys=True, indent=4, separators=(',', ': '))

