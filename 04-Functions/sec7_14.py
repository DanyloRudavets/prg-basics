n1=2
n2=3
o="**"
def calc(n1,n2,o):
    if o=='+':
        return n1+n2
    elif o=='-':
        return n1-n2
    if o=='*':
        return n1*n2
    elif o=='**':
        return n1**n2
    if o=='/':
        return n1/n2
    elif o=='//':
        return n1//n2
    if o=='%':
        return n1%n2