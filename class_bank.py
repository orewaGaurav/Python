class BankAcc:
    bank_name = "Default Bank"

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdrawl(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}.")
        else:
            print("Amount can't be withdrawn!")

    def display_account_details(self):
        print(f"Bank: {BankAcc.bank_name}")
        print(f"Balance: {self.balance}")
        
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name}.")

    @staticmethod
    def validate_account_number(account_number):
        if isinstance(account_number,int) and len(str(account_number)) == 10:
            print("Account number is valid.")
            return True
        else:
            print("Invalid account number. Must be a 10-digit number.")
            return False

account1 = BankAcc("Priyanshu Kumar", 100000)
account1.display_account_details()

account1.deposit(200)

account1.withdrawl(100)

account1.display_account_details()

BankAcc.change_bank_name("HDFC Bank")

account1.display_account_details()

BankAcc.validate_account_number(1234567890)
BankAcc.validate_account_number(12345)