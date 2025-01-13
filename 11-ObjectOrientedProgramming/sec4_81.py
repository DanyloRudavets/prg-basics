from sec4_8 import Contact

class Contact_list:
    def __init__(self):
        self.list=[]
    def add(self, name, email,telephone):
        newc=Contact(name,email, telephone)
        self.list.append(newc)
    def display(self):
        for i in self.list:
            print(i)
