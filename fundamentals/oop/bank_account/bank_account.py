class BankAccount:
    bank_name = "Dojo Bank"

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insuficient Funds: $5 fee charged")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Current Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

account_01 = BankAccount(0.02, 30000)
account_02 = BankAccount(0.067, 5500)

account_01.display_account_info().deposit(200).deposit(250).deposit(4350).withdraw(1500).display_account_info()

account_02.display_account_info().deposit(20).deposit(200).withdraw(3500).withdraw(1230).withdraw(275).withdraw(1000).display_account_info()
