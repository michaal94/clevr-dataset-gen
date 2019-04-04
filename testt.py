import json

path = "/home/michas/Desktop/datasets/clevr/CLEVR_v1.0/questions/CLEVR_val_questions.json"

with open(path, 'r') as f:
    a = json.load(f)

for i in range(3000):
    if a['questions'][i]['question_family_index'] == 0:
        print(i, a['questions'][i]['question'])
