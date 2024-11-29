def bublesort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] >a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
print(bublesort([4,36,12,28,9,44,5]))