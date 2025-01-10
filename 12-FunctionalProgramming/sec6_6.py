n=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
def f(n):
    for i in n:
        print(f'{i[0].upper()}, {i[1]}')
f(n)