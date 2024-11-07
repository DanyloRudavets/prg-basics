a='20345674'
c=0
for i in range(len(a)):
    for g in range(len(a)-1):
        if a[i]==a[g]:
            c=c+int(a[i])
print(c)