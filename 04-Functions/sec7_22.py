def f(name):
    c=name[0]
    for i in range(len(name)):
        if name[i]==' ':
            c=c+name[i+1]
    return c
print(f("Internet of Things"))
print(f("For Your Information"))