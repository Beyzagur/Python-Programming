import imp
from CreditAccounts import CreditAccount as creditAccount

class Customer:
    def __init__(self, accountID, name, totalAmount=0):
        self.accountID=accountID
        self.name=name
        self.totalAmount=totalAmount
        self.bankAccount=creditAccount(accountID, name, 1000, totalAmount)