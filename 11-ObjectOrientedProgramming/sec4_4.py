class EBOOK:
    def __init__(self,title,author,nop,cpn=0):
        self.title=title
        self.author=author
        self.nop=nop
        self.cpn=1
        self.oc=False
    def book_open(self):
        self.oc=True
        return self.oc
    def book_close(self):
        self.oc=False
    def book_status(self):
        return f'{self.title},{self.author},{self.nop},{self.cpn}'
    def page_up(self):
        if self.cpn<self.nop:
            self.cpn+=1
        return self.cpn
    def page_down(self):
        if self.cpn>1:
            self.cpn=self.cpn-1
        return self.cpn
    

        