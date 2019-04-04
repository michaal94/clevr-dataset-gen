import pycocotools.mask as mask_utils
import cv2
import numpy as np
import os
import json

scene_file = "../output/scenes/CLEVR_new_000001.json"
img_file = "../output/images/CLEVR_new_000001.png"

with open(scene_file, 'r') as f:
    props = json.load(f)

img = cv2.imread(img_file)
# cv2.imshow('asdf', img)
# cv2.waitKey(0)

print(props)

font = cv2.FONT_HERSHEY_SIMPLEX

for i, obj in enumerate(props['objects']):
    name = obj['shape']
    mask = obj['mask']
    mask = mask_utils.decode(mask)
    mask = 255 * mask.astype(np.uint8)
    mask = np.repeat(np.expand_dims(mask, 2), 3, axis=2)
    cv2.putText(mask, name, (10, 470), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(mask, obj['size'], (10, 440), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(mask, obj['material'], (10, 410), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(mask, obj['color'], (10, 380), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow(str(i) + ' - ' + name, mask)
    cv2.waitKey(10)


cv2.waitKey(0)
