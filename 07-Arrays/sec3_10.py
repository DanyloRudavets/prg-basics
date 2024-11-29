n1=[4,36,12,28,9,44,5]
n2=[5,1,36]
for i in n2:
    if i in n1:
        n1.remove(i)
print(n1)