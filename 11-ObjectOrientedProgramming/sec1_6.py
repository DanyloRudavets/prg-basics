class Phone():
    def __init__(self,on, executing: str):
        self.on= on
        self.executing= executing
    def ison(self):
        return self.on
    def exc(self):
        return self.executing
phone1=Phone(True, 'Pornhub')
print(phone1.ison())
print(phone1.exc())
