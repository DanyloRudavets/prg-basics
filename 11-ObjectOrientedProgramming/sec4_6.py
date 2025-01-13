class BANKAcc:
    def __init__(self, account):
        self.account=account
        self.balance=0
    def display_bal(self):
        return self.balance
    def deposit_m(self, n):
        self.balance+=n
        return self.balance
    def withdraw_m(self,n):
        if self.balance>=n:

            self.balance-=n
            return self.balance
        else:
            return None
    
    
    

        