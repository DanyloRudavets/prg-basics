twitter= False
instagram= False
facebook=False
youtube=False
g=1
y=1
k=1
t=1
a= input('do u have twitter(y/n):')
b=input('do u have instagram(y/n):')
c=input('do u have facebook(y/n):')
f=input('do u have youtube(y/n):')
if a== 'y':
    twitter==True
elif a=='n':
    g=0
print(f'Twitter ={twitter}')
if b== 'y':
    instagram==True
elif b== 'n':
    y=0
print(f'Instagram ={instagram}')
if c=='y':
    facebook==True
elif c== 'n':
    k=0
print(f'Facebook ={facebook}')
if f== 'y':
    youtube==True
elif f=='n':
    t=0
print(f'youtube ={youtube}')
if g==1:
    if k==1 or t==1 or y==1:
        print('you are a good influencer')
else:
    print('still not on the right level')