def f(n):
    l = []
    num = 1
    while len(l) < n:
        num += 1
        prime = True
        for i in range(2, num):
            if prime and num % i == 0:
                prime = False
        if prime:
            l.append(num)
    return l

print(f(1))
print(f(5))