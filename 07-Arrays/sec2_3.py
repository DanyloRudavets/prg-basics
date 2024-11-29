# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
tm=0
tf=0
tt=0
tu=0
# Calculates expenses
# Use loop statements
for i in monthly_expenses:
    for j in i:
        tm+=j
for i in monthly_expenses:
    tf+=i[0]
    tt+=i[1]
    tu+=i[2]
tw1=0
tw2=0
tw3=0
tw4=0
for i in monthly_expenses:
    if i==monthly_expenses[0]:
        for j in i:
            tw1+=j
    elif i==monthly_expenses[1]:
        for j in i:
            tw2+=j
    if i==monthly_expenses[2]:
        for j in i:
            tw3+=j
    if i==monthly_expenses[3]:
        for j in i:
            tw4+=j

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',tf)
print('Transport:', tt)
print('Utilities:', tu)
print('Week 1:', tw1)
print('Week 2:', tw2)
print('Week 3:', tw3)
print('Week 4:', tw4)
print('---------------')
print('TOTAL:', tm)