n=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
long=n[0]
for i in range(len(n)):
    if len(long)<len(n[i]):
        long=n[i]
print(long)
