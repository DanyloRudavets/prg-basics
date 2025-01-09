import json
with open('dogs.json','r',  encoding='utf-8')as file:
    data=json.load(file)
    for i in data:
        if i['age']<5:
            print(i)
            
