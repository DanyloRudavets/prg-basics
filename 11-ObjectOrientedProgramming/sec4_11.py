class C:
    def __init__(self,d):
        self.d=d
    def m1(self,s,n):
        self.d[s]=n
        
        return self.d
    def m2(self,s):
        g=0
        s.split()
        for i in s:
            if i in self.d:
                g+=self.d[i]
        return g
        