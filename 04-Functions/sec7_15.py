n='+--+-++-----'
c=False
def calc(n,c):
    for i in range(len(n)):
        if n[i]=='+':
            if n[i+1]=='+':
                if n[i+2]=='+':
                    c=True
    return c
