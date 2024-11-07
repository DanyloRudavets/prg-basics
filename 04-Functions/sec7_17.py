a='radbar'
b=''
g=False
def calc():
    b=''
    for i in a:
        b=b+i
    if b ==a:
        g=True
    print(g)
calc()