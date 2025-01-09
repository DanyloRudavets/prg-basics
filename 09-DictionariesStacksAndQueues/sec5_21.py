import json
data={
    'key':
    3,
    't':False,
    'rr':None
}
with open ('favourite.json', 'w')as file:
    json.dump(data,file)