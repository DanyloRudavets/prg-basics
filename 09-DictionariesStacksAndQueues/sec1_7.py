list={
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
c=0
for p,q in list.items():
    print(f'{p} {q}')
for q in list.values():
    c+=q
print(c)
