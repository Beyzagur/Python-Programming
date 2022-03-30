from BankAccounts import BankAccount

class CreditAccount(BankAccount):
    def __init__(self, accountID, owner, limit, totalAmount=0):
        super().__init__(accountID, owner, totalAmount)
        self.limit=limit
    def creditWithdrawal(self, amount):
        if self.limit-amount>=0:
            self.limit-=amount
        else:
            print("You have not enough limit on credit cards.")
    def display(self):
        super().display()
        print("Limit : {}".format(self.limit))