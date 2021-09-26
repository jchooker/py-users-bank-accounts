class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.01, 1000)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f"Account balance for {self.name}: {self.account}")
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        return self

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        print("New account successfully created!")
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! New balance: $",end="")
        print("%.2f"%self.balance)
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print(f"Insufficient funds in account! $5 penalty will be assessed! \n New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: $",end="")
        print("%.2f"%self.balance)
        return self
    def display_account_info(self):
        print(f"Current account balance: $",end="")
        print("%.2f"%self.balance)
        return self
    def yield_interest(self):
        ydInt = self.balance*self.int_rate
        self.balance += ydInt
        print("$"+"%.2f"%ydInt,end="")
        print(" interest added!")
        return self

joseph = User("joseph", "jcole@ualr.giz")

# def accountMenu():
#     goodInput = False
#     while not goodInput:
#         input("Please provide name for user account:")

