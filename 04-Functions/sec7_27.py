def f(pc):
    c=True
    s=int(pc[0])+int(pc[1])+int(pc[2])
    if s%7!=int(pc[3]):
        c=False
    return c
print(f("1114"))
