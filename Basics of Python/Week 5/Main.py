from Customers import Customer

customer1=Customer(1,"Beyza GUR", 8000)
customer2=Customer(2,"Osman Mutlu", 6000)

customer1.bankAccount.display()
print("______________________________")
customer2.bankAccount.display()

customer1.bankAccount.withdraw(700)
customer1.bankAccount.creditWithdrawal(1000)
customer2.bankAccount.withdraw(300)
customer2.bankAccount.creditWithdrawal(500)
print("\n**---------------------------**\n")
customer1.bankAccount.display()
print("-------------------------")
customer2.bankAccount.display()