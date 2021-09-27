class User:
    def __init__(self, name, email, startBal=0):
        self.name = name
        self.email = email
        self.account = BankAccount(0.01, startBal)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f"Account balance for {self.name}: $",end="")
        print("%.2f"%self.account.balance)
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

def runMenu():
    acct_name = input("Please provide name for user account: ")
    acct_email = input("Please provide email for account: ")
    validEmail = emailVerified(acct_email)
    while not validEmail:
        acct_email = input("Invalid email! Please provide email for account: ")
        validEmail = emailVerified(acct_email)
    # acct_type = input("Which type of account? (C)hecking or (S)avings: ")
    # validAcct = validAcctTypeSel(acct_type)
    # print(validAcct)
    # while not validAcct:
    #     acct_type = input("Invalid account selection! Please choose (C)hecking or (S)avings: ")
    #     validAcct = validAcctTypeSel(acct_type)
    # acct_type = acctTypeSel(acct_type)
    init_bal = validateBal(input("How much to deposit for initial balance? : $"))

    return User(acct_name, acct_email, init_bal)

def emailVerified(strTest): #incomplete email test
    atTest = "@"
    dotTest = "."
    if atTest in strTest:
        j = strTest.index(atTest)
        if dotTest in strTest[j+len(atTest):]:
            return True
    return False

# def validAcctTypeSel(strTest):
#     return strTest == "c" strTest == or "C" or "s" or "S")

# def acctTypeSel(strTest):
#     if strTest == "c" or "C":
#         return "Checking"
#     elif strTest == "s" or "S":
#         return "Savings"

def validateBal(inputTest):
    while True:
        try:
            val = int(inputTest)
            return val
        except ValueError:
            try:
                val = float(inputTest)
                return val
            except ValueError:
                print("Invalid input! Please provide valid amount!: ")

def addUserOption():
    userInput = input("Would you like to add an account? (Y)es or (N)o: ")
    validInput = False
    if (userInput == "Y") or (userInput == "y") or (userInput == "N") or (userInput == "n"):
        validInput = True
    while not validInput:
        userInput = input("Invalid entry! Would you like to add another account? (Y)es or (N)o: ")
        if (userInput == "Y") or (userInput == "y") or (userInput == "N") or (userInput == "n"):
            validInput = True
    if (userInput == "Y") or (userInput == "y"):
        return True
    else:
        return False

user_list = []
while addUserOption():
    user_list.append(runMenu())
for i in user_list:
    i.display_user_balance()

