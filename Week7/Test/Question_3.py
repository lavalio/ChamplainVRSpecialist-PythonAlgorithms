#Creat a class called BankAccount


class BankAccount:
    balance = 0

    def __init__(self,input_balance = 0):
        self.balance = input_balance

    def deposit(self, val):
        self.balance += val

    def withdraw(self, val):
        self.balance -= val

b = BankAccount(10)
b.deposit(25)
b.withdraw(1)

print("The balance of the bank account is now " + str(b.balance))

print("*****Another Account*****")
b = BankAccount()
b.deposit(25)
print("The balance of the bank account is now " + str(b.balance) + " after deposit")
b.withdraw(6)
print("The balance of the bank account is now " + str(b.balance) + " after withdraw")