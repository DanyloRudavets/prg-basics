def f(n):
    l=[]
    for i in  range(len(n[0])):
        c=0
        for j in range(len(n)):
            c+=n[j][i]
        l.append(c)
    for i in l:
        if l.count(i)>=2:
            k=True
            break
        else:
            k=False
    return k

print(f([[3,4],[5,1],[4,7]]))
print(f([[3,4],[5,9],[4,7]]))
print(f([[3,4,2],[5,1,6]]))
        
