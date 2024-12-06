countries = [
{"name":"Poland", "population":38000000},
{'name':"China", 'population': 1409670000},
{'name':'India', 'population':1404910000},
{'name':'US', 'popuation': 350000000},
{'name':'Brazil', 'population': 200000000}
]
print('Country',end=' ')
print('Population')
for i in countries:
    for n,p in i.items():
        print(f'{n} {p}')