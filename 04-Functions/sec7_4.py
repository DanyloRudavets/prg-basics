n='You never get a second chance to make a first impression'
c=0
def calc(n,c):
    for i in range(0,len(n)):
        if n[i]=='e':
            c+=1
    print(c)
