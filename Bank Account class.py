class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def show(self):
        print(self.owner,self.__balance)
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance-=amount
        else:
            print("invalid amount")