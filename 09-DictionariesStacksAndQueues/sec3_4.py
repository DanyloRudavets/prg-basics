
def b(n):
    import queue
    c=queue.LifoQueue()
    q=1
    while q!=0:
        q=n//2
        c.put(n%2)
        n=q
    while not c.empty():
        r=c.get()
        print(r)
b(18)
        