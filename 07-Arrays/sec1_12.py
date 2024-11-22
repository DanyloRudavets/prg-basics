categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
b=max(expenses)
c=0
for i in range(len(expenses)):
    if  expenses[i]==b:
        c=i
print(categories[c])
print(categories[expenses.index(max(expenses))])