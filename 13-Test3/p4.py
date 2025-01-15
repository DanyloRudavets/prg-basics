def f(fn,prd):
    x=list(map(fn,prd))
    return x
print(f(lambda x: "id:"+x[:2],["water","cheese","tomato"]))
print(f(lambda x: (x[0]+x[-1]).upper(),["water","cheese","tomato"]))