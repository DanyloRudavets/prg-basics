
# def f(n):
#     num=['1','2','3','4','5','6','7','8','9','0']
#     und='_'
#     if len(n)>=1 and len(n)<=5:
#         if n[0].lower()!=n[0].lower() or n[0]!=und:
#             c=False
#         else:
#             for i in range(len(n)):
#                 if n[i].upper()!=n[i].upper() or n[i] not in num or n[i]!=und:
#                     c=False
#                     break
#                 else:
#                     c=True
#     else:
#         c=False
#     return c
# print(f("abc"))

def f(variable):
    import re
    if len(variable)>=1 and len(variable)<=5:
        pattern='^[a-zA-Z]|_+[\d\w_]+'
        a=re.match(pattern,variable)
        if a:
            print(True)
        else:
            print(False)
    else:
        print(False)

f('abc')
f('Abc')
f('aBc')
f('_ab_c')
f('abcdef')
f('8abc')
f('_aB8_')
f('_4x_')

