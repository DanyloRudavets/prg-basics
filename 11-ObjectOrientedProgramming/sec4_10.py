class C:
    def __init__(self,list):
        self.list=list
    def m(self,n):
        ok=0
        for i in self.list:
            k=0
            for j in i:
                if j>0:
                    k+=1
            if k==2:
                ok+=1
        if ok>=n:
            return True
        else:
            return False


        