import re
file = 'files.txt'
with open(file, 'r')as file:
    content=file.read()
    c=content.splitlines()
for i in c:
    p='^(\w{4}_)'
    g=re.findall(p,i)
    if g:
        print(g)