n=[15,8,31,47,2,19]
i=0
c=0
while i!=len(n):
    c+=n[i]
    i+=1
print(c)
print(f'{c//len(n):.2f}')
