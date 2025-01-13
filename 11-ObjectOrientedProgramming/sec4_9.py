class C:
    def __init__(self,name,surname,age,seniority):
        self.name=name
        self.surname=surname
        self.age=age
        self.seniority=seniority
    def __str__(self):
        if self.age<18:
            s=self.surname
            n=self.name
            return f'{s.lower()}{n[0].lower()}{self.seniority}'
        else:
            s=self.surname
            n=self.name
            return f'{s.upper()}{n[0].upper()}{self.seniority}'


        