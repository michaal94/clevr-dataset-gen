import json

with open('./data/object_properties.json', 'r') as f:
    objects_dict = json.load(f)

name_to_num = dict()

i = 1
for obj in objects_dict.keys():
    if objects_dict[obj]['name'] not in name_to_num:
        name_to_num[objects_dict[obj]['name']] = i
        i += 1

reversed_dict = {v: k for k, v in name_to_num.items()}

with open('./obj_name_to_num.json', 'w') as f:
    json.dump(name_to_num, f, sort_keys=True, indent=4, separators=(',', ': '))
