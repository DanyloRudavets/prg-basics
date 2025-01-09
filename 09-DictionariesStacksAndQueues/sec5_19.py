import json
with open('reservations.json','r',encoding='utf-8')as file:
    content=json.load(file)
def nr(content):
    c=0
    for i in content['reservations']:
            c+=1
    print(c)
nr(content)
def pr(content):
    c=0
    for i in content['reservations']:
        if i['paid']==True:
             c+=1
    print(c) 
pr(content)
         
def upr(content):
    c=0
    for i in content['reservations']:
        if i['paid']==False:
             c+=1
    print(c) 
upr(content)

def vpr(content):
    c=0
    for i in content['reservations']:
        if i['paid']==True:
            c+=i['price_per_night']*i['nights']
    print(c)
vpr(content)

def uvpr(content):
    c=0
    for i in content['reservations']:
        if i['paid']==False:
            c+=i['price_per_night']*i['nights']
    print(c)
uvpr(content)