# Question 3 – Classes and Objects
# 1)	Create a class called BankAccount.
# 2)	The bankaccount has only 1 property (variable) which is “balance”.
# 3)	Balance should be set to the initial value at creation, or 0.
# 4)	Two methods should exist, “deposit” and “withdraw”.
# These two function just increment and decrement the value of balance depending on what we give them.


class BankAccount:
    """Bank account class with deposit and withdraw methods."""
    #balance = 0.00

    def __init__(self, amount = 0.01):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


b = BankAccount(10)
b.deposit(25)
b.withdraw(1)
print("The balance of the bank account is now " + str(b.balance))
