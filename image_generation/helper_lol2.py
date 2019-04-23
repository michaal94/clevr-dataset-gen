import os
import json

path = '/home/michas/Desktop/datasets/shop_vqa_test/scenes'

i=1
for scene in sorted(os.listdir(path)):
    with open(os.path.join(path, scene), 'r') as f:
        scene_data = json.load(f)
        img_name = scene_data['image_filename']
        if 'CLEVR' in img_name:
            print('hit %d %s' % (i, scene))
            i += 1
            new_name = img_name.replace("CLEVR", "SHOP_VQA")
            #print(new_name)
            scene_data['image_filename'] = new_name
            #print(scene_data)
    #with open(os.path.join(path, scene), 'w') as f:
    #   json.dump(scene_data, f)


