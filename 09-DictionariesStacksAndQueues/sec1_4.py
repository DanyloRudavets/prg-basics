person={
    'name':"Danylo",
    'surname':"Rudavets",
    'age':17,
    'hobby':['reading','sleeping'],
    'married': False,
    'phone':{'Company':"Apple","Model":13}
}
print(person['name'])
print(person['hobby'])
print(person)
person['surname']='Novak'
person['married']=True
person['gender']='male'
person['hobby'].append('bicycle')
person['phone']['new']=2
print(person)