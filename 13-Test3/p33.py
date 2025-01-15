def f(n):
    c=0
    l=0
    for i in n.values():
        c+=i
    k=c/len(n)
    for i in n.values():
        if i>k:
            l+=1
    return l
print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))
