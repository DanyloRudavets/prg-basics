def f(mnumber):
    
    k=0
    a=['a','b','c','d','A','B','C','D']
    n=['1','2','3','4','5','6','7','8','9','0']
    for i in mnumber:
        c=0
        if len(i)>=1 and len(i)<=7:
            for j in i:
                if j in a or j=='-' or j=='+' or j in n:
                    c+=1
        if c==len(i):
            k+=1
    return k
print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))



