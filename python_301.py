#! /usr/bin/python3


# TODO: create a banking class
class Banking:
    
    accounts = {}
    
    def __init__(self, name):
        self.name = name
        self.balance = 0

# TODO: add withdraw function
    def withdraw(self, amount):
        if amount <= self.balance:
            print(f"\nwithdrawing {amount}$ from {self.name} account.")
            self.balance -= amount
            print('Done.')
        else:
            print('\naccount balance is insufficient.')
        self.show_balance()

# TODO: add deposit function
    def deposit(self, amount):
        if amount > 0:
            print(f'\nadding {amount}$ to the {self.name} balance.')
            self.balance += amount
            print('Done.')
        else:
            print("\ninvalid value.")
        self.show_balance()
            
# TODO: show current accounts
    @classmethod
    def show_accounts(self):
        print()
        for i, k in enumerate(Banking.accounts):
            print(f"{i}. {k}")
        print()
        
# TODO: show account balance
    def show_balance(self):
        print()
        print(f"Your balance is : {self.balance}")
        print()
        
        

# TODO: put it in a while loop
while True:
    # TODO: for each action ask for user input
    account_req = input("1.Available account\n2.Opening new account\n3.show accounts\nEnter intended number: ")
    try:
        account_req = float(account_req)
    except Exception:
        print("Invalid value")
    else:
        if account_req == 1:
            account_name = input('Enter name of your account: ')
            account = Banking.accounts.get(account_name)
            if account:
                operation = input("1.withdraw\n2.deposit\n3.show balance\nEnter operation number: ")
                try:
                    operation = float(operation)
                except Exception:
                    print("Invalid value")
                else:
                    if operation == 1:
                        amount = input("How much do you wanna withdraw ? ")
                        try:
                            amount = float(amount)
                        except:
                            print("Invalid value")
                        else:
                            account.withdraw(amount)
                    elif operation == 2:
                        amount = input("How much do you wanna deposit ? ")
                        try:
                            amount = float(amount)
                        except:
                            print("Invalid value")
                        else:
                            account.deposit(amount)
                    elif operation == 3:
                        account.show_balance()
                    else:
                        print("Invalid value")
            else:
                print("Account Not Found.")
        elif account_req == 2:
            new_account_name = input("What's your new account name? ")
            new_account = Banking(new_account_name)
            Banking.accounts[new_account_name] = Banking(new_account_name)
        elif account_req == 3:
            Banking.show_accounts()
        else:
            print('Request is not valid.')