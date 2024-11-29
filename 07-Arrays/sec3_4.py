n=[-15,8,-31,47,-2,19]
max=n[0]
min=n[0]
for i in range(len(n)):
    if max<n[i]:
        max=n[i]
    elif min>n[i]:
        min=n[i]
print(max)
print(min)