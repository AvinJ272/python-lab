class bankaccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.account_number = acc_no
        self.name=name
        self.account_type = acc_type
        self.balance = balance


    def deposit(self,amount):
        if amount <= 0:
            print("deposit amount must be postive")
        else:
            self.balance += amount
            print(f"deposit: {amount}")

            print(f"Updated balance:{self.balance}")


    def withdraw(self,amount):
        if amount <=0:
            print("withdrawal amount must be positive")
        elif self.balance < amount:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"withdrew:{amount}")
            print(f"updated balance:{self.balance}")

    def display(self):
        print("\nAccount details:")
        print(f"account number:{self.account_number}")
        print(f"Account holder: {self.name}")
        print(f"Account type:{self.account_type}")
        print(f"Account Balance: {self.balance}")

acc_no = int(input("enter the account number:"))
name = input("enter the account holder name:")
acc_type = input("enter the account type(saving/current):")
balance = int(input("enter the initial balance:"))

account = bankaccount(acc_no, name, acc_type, balance)

account.display()

deposit_amount = int(input("\nEnter the amount to deposit:"))
account.deposit(deposit_amount)


withdraw_amount = int(input("\Enter the amount to withdraw:"))
account.withdraw(withdraw_amount)