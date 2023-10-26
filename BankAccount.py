class BankAccount:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self) # Allows for class method to access attributes

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance -amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging $5 fee!")
            self.balance = self.balance - 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            added_int = self.balance * self.int_rate
            self.balance += added_int
        return self
    
    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

User_1 = BankAccount(.10, 200)
User_2 = BankAccount(.05, 1000)

User_1.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info()
User_2.deposit(40). deposit(50).withdraw(200).withdraw(100).withdraw(50).withdraw(30).yield_interest().display_account_info()

#display all accounts
BankAccount.all_accounts()

class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s Balance: {self.account.balance}")
        return self


User_3 = User("kenny", "kenny@email.com")

User_3.make_deposit(200).make_withdrawal(15).display_user_balance()



