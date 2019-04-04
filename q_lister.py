import json

path = "./question_generation/CLEVR_1.0_templates/compare_integer.json"

with open(path, 'r') as f:
    questions = json.load(f)

for q in questions:
    print(q['text'])
