import os
import json

path = '/home/michas/Desktop/datasets/full_shop/scenes'

i=1
for scene in sorted(os.listdir(path)):
    with open(os.path.join(path, scene), 'r') as f:
        scene_data = json.load(f)
    for obj in scene_data['objects']:
        if obj['color'] == 'metalllic':
            print("hit %d %s" % (i, scene))
            i += 1
#            obj['color'] = 'metallic'
#    with open(os.path.join(path, scene), 'w') as f:
#        json.dump(scene_data, f)


