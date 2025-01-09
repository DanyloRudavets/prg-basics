basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}
person={}
for k,v in basic_data.items():
    person[k]=v
for k,v in advanced_data.items():
    person[k]=v
print(person)