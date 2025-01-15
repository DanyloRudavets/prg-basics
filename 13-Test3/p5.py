class C:
    def __init__(self,n):
        self.n=n
    def m1(self):
        print(self.n)
    def m2(self):
        self.n+=1
        return self.n
    def m3(self):
        self.n-=1
        return self.n
    def m4(self,e):
        self.n+=e
        return self.n
    def __str__(self):
        return 'f{self.n}'
c=C(5)
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1()
c.__str__()