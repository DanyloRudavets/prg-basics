class Statistics:
    def __init__(self):
        self.list=[]
    def add_num(self, n):
        self.list.append(n)
        return self.list
    def space_num(self):
        for i in self.list:
            print(i, end=' ') 
    def great(self):
        return max(self.list)
    def lower(self):
        return min(self.list)
    def mean(self):
        g=0
        for i in self.list:
            g+=i
        return g/(len(self.list)-1)
    def median(self):
        return self.list[len(self.list)//2]
    
