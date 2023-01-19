import json

rows = json.load(open("dadjokes.json", 'r', encoding='utf-8'))
id='c9aaad4d'
for x in rows:
    value_list=[]
    for value in x.values():
        value_list.append(value)
    if id==value_list[0]:
        print(x)
    # if x[0]==id:
    #     print(found)