def f(uid):
    k=[]
    c= True
    for i in uid:
        if i in  k:
            c=False
            return c
        else:
            k.append(i)
            c=True
    return c
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","BOB2"]))
print(f(["bob2","bob2"]))