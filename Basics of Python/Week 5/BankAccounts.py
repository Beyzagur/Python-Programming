from sympy import total_degree

class BankAccount:
    def __init__(self, accountID, owner, totalAmount=0):
        self.accountID=accountID
        self.owner=owner
        self.totalAmount=totalAmount
    def withdraw(self, amount):
        self.totalAmount-=amount
    def deposite(self, amount):
        self.totalAmount+=amount
    def display(self):
        print("Account ID :",self.accountID)
        print("Owner :",self.owner)
        print("Total amount :",self.totalAmount)