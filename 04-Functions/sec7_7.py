
def calc(g):
    c=True
    for i in range(len(g)):
        if not (g[i]=='1' or g[i]=='0') and c:
            c=False 

    return c