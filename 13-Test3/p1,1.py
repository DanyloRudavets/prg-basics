def f(n):
    c=n.lower()
    for i in range(len(n)):
        print(f'{c[:i]}{c[i].upper()}{c[i+1:]}', end='-')
f('book')
f('water')
f('ok')