def f(p):
    c=True
    g=''
    k=0
    if len(p)>=6:
        for i in range(len(p)):
            g+=p[i]
            if p[i] in g:
                k=g.count(p[i])
                if k>=2:
                    c=False
    else: 
        c=False
    return c
print(f("ax15"))
print(f("A2water3"))
print(f("qwerty"))
print(f(''))