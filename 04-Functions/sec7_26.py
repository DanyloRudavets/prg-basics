def f(text):
    c=''
    for i in range(len(text)):
         c=c+text[i]+'-'
    return c[:-1]
print(f("University"))