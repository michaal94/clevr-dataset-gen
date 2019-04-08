import os
import json

import pandas as pd

df = pd.read_csv('./objects_2.csv')
print(df.head())
# print(df['Object name'])


shapes_list = sorted(os.listdir('./data/shapes'))
for i in reversed(range(len(shapes_list))):
    if '.blend' not in shapes_list[i]:
        shapes_list.pop(i)

# for i in range(len(shapes_list)):
#     print(shapes_list[i])

objects = dict()

for i in range(len(shapes_list)):
    # text = "obj%02d" % (i + 1)
    obj = shapes_list[i].split('.')[0]
    obj_name = ''.join(c for c in obj if not c.isdigit())
    obj_name = ''.join(c if c != '_' else ' ' for c in obj_name)
    obj_name_df = ''.join(c if c != '_' else ' ' for c in obj)
    obj_name_df = ''.join(c if not c.isdigit() else (' ' + c) for c in obj_name_df).capitalize()
    # print(obj_name_df)
    obj_change_mat = df[df['Object name'] == obj_name_df]['Material change'].item()
    print(obj_change_mat)
    obj_material1 = df[df['Object name'] == obj_name_df]['Material 1 (default)'].item().lower()
    obj_material2 = df[df['Object name'] == obj_name_df]['Material 2'].item().lower()
    obj_change_col1 = df[df['Object name'] == obj_name_df]['Color1 change'].item()
    obj_change_col2 = df[df['Object name'] == obj_name_df]['Color2 change'].item()
    # print(obj_change_col1, obj_change_col2)
    obj_color1 = df[df['Object name'] == obj_name_df]['Colors - material 1'].item().lower()
    obj_color2 = df[df['Object name'] == obj_name_df]['Colors - material 2'].item().lower()
    print(obj_color1, obj_color2)
    obj_change_size = df[df['Object name'] == obj_name_df]['Size change'].item()
    weight = df[df['Object name'] == obj_name_df]['Weight'].item().lower()
    movement = df[df['Object name'] == obj_name_df]['Movability'].item().lower()
    shape = df[df['Object name'] == obj_name_df]['Shape'].item().lower()
    size1 = df[df['Object name'] == obj_name_df]['Size 1'].item().lower()
    size2 = df[df['Object name'] == obj_name_df]['Size 2'].item().lower()
    objects[obj] = {
        'name': obj_name,
        'change_material': obj_change_mat,
        'change_size': obj_change_size,
        'change_color1': obj_change_col1,
        'change_color2': obj_change_col2,
        'material1': obj_material1,
        'material2': obj_material2,
        'color1': obj_color1,
        'color2': obj_color2,
        'size1': size1,
        'size2': size2,
        # 'size_change': size_change,
        'weight': weight,
        'movement': movement,
        'shape': shape
    }

print(objects)


with open('./object_properties.json', 'w') as f:
    json.dump(objects, f, sort_keys=True, indent=4, separators=(',', ': '))

