import json


with open('FilesVRA/vra.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

for d in dados:
    print(d['icaoaeródromo_origem'], d['icaoaeródromo_destino'])

