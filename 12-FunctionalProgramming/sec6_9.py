k={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
# j=list(filter(lambda x: x>0, k.values()))

# print(list(map(lambda x: j[x], k.items)))
def f(k):
    for i,j in k.items():
        if j>0:
            print(i)
f(k)
