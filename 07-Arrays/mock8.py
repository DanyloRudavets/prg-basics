def f(k):
    c=0
    b=[]
    h=0
    n=list(k)
    for i in range(len(str(n))):
        if n[i]=='+':
            c=c+n[i-2]+n[i-4]
            b.append(c)
            if n[i+1]=='+':
                h+=1
                c=c+b[h]
            if n[i+1]=='-':
                h+=1
                c=c-b[h]
        if n[i]=='-':
            c=c-n[i-2]-n[i-4]
            b.append(c)
            if n[i+1]=='+':
                h+=1
                c=c+b[h]
            if n[i+1]=='-':
                h+=1
                c=c-b[h]
        return c
    
print(f("2 6 + 4 5 - +"))
n="2 6 + 4 5 - +"
print(list(n))
