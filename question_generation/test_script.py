import json

path= '/home/michas/Desktop/datasets/shop_vqa/questions/SHOP_VQA_test_questions.json'

with open(path, 'r') as f:
    qs = json.load(f)

print(len(qs['questions']))
print('asd')
