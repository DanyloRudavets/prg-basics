paragraph = "cat dog mouse cat rat cat mouse"
...
...
c=paragraph.split()
d={}
k=0
for i in c:
    d.update({i:4})
for i in d:
    k=c.count(i)
    d[i]=k

print(d)