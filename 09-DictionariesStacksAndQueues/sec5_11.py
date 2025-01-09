import json
g={
   'person_name': 'number of votes',
   'person_name': 'number of votes',
}
file='voting.json'
# Read the contents of the json file
with open(file, 'r')as file:
    content=json.load(file)


# Vote for a person
person_name = input('Name of the person you are voting for:')
# Save voting data to json file
with open(file, 'w')as file1:
    json.dump(g)