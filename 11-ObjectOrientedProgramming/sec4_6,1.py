from sec4_6 import BANKAcc
acc1=BANKAcc('12 3456 5555 9090 1111 0000 7722')
print(BANKAcc.display_bal(acc1))
BANKAcc.deposit_m(acc1, 25.3)
print(BANKAcc.display_bal(acc1))
BANKAcc.withdraw_m(acc1, 31.70)
print(BANKAcc.display_bal(acc1))
BANKAcc.withdraw_m(acc1,14)
print(BANKAcc.display_bal(acc1))
