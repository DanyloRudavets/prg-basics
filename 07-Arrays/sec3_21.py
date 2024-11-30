a1=[7,3,3,2,3,3,4]
a2=[7,3,8,5,2]
k=[]
c=False
for i in a1:
    if i in a2:
        k.append(i)
if len(k)==len(a1):
    c=True
print(c)