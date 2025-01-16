class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.q=0
    def m1(self):
        if self.x>0 and self.y>0:
            self.q=1
        elif self.x>0 and self.y<0:
            self.q=4
        if self.x<0 and self.y<0:
            self.q=3
        elif self.x<0 and self.y>0:
            self.q=2
        if self.x==0 or self.y==0:
            self.q=0
        return self.q
    def m2(self,a,b):
        qq=0
        if a>0 and b>0:
            qq=1
        elif a>0 and b<0:
            qq=4
        if a<0 and b<0:
            qq=3
        elif a<0 and b>0:
            qq=2
        if a==0 or b==0:
            qq=0
        elif qq==self.q:
            print(True)
        if qq!=self.q:
            print(False)
    def m3(self,a,b):
        import math
        d=math.sqrt((abs(abs(self.x)-abs(a))**2+(abs(abs(self.y)-abs(b)))**2))
        if d>5:
            print(True)
        else:
            print(False)
        



