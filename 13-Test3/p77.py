def f(n):
    l=[]
    k=''
    for i in n:
        if i[0] in l:
            l.pop(l.index(i[0]))
        elif i[1]=='in':
            l.append(i[0])
    return sorted(l)

print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]))
print(f([["KR234","in"],["KR234","out"]] 
))