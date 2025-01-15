def f(f,n):
    x=list(filter(f,n))
    if  len(x)==0:
        return -1
    else:
        return max(x)-min(x)
print(f(lambda x: x>50, [95,90,20,50,70]))
print(f(lambda x: x>30 and x<90, [95,90,20,50,70]))