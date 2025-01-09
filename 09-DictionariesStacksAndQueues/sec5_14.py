import queue
c=queue.Queue()
n=4
for i in range(1,n):
    c.put(i)

print(f'your number is {c.get()} ')
