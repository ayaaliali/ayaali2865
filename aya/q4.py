class BankAccount:
    def init(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def str(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}"

# تعريف الفئة الفرعية SavingsAccount


class SavingsAccount(BankAccount):
    def init(self, account_number, account_holder, interest_rate, balance=0.0):
        super().init(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Applying interest: ${interest}")
        self.deposit(interest)

    def str(self):
        return super().str() + f", Interest Rate: {self.interest_rate}%"


# إنشاء مثال من BankAccount
account = BankAccount(123456, "John Doe")
account.deposit(1000)
account.withdraw(500)
print(account)

# إنشاء مثال من SavingsAccount
savings_account = SavingsAccount("789012", "Jane Doe", interest_rate=5)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)
