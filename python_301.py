#! /usr/bin/python3


# TODO: create a banking class
class Banking:
    
    __accounts = {}
    
    def __init__(self, name, password):
        self.name = name
        self.password =  password
        self.balance = 0
        Banking.__accounts[self.name] = self
        

    # TODO: add withdraw function
    def withdraw(self, amount):
        if amount <= self.balance:
            print(f"\nwithdrawing {amount}$ from {self.name} account.")
            self.balance -= amount
            print('Done.')
            self.logging("withdraw", f"-{amount}")
        else:
            print('\naccount balance is insufficient.')
        self.show_balance()

    # TODO: add deposit function
    def deposit(self, amount):
        if amount > 0:
            print(f'\nadding {amount}$ to the {self.name} balance.')
            self.balance += amount
            print('Done.')
            self.logging('deposit', f"+{amount}")
        else:
            print("\ninvalid value.")
        self.show_balance()
            
    # TODO: show current accounts
    @classmethod
    def show_accounts(cls):
        print()
        if cls.__accounts:
            for i, k in enumerate(Banking.__accounts):
                print(f"{i}. {k}")
        else:
            print("No account registered.")
        print()
        
    # TODO: show account balance
    def show_balance(self):
        print()
        print(f"Your balance is : {self.balance}")
        print()
        
    # TODO: adding log
    def logging(self, operation, amount):
        with open(f"{self.name}.txt", 'a') as f:
            f.write(f"{operation} ---------------------------> {amount}\n")
        
    # TODO: showing log file
    def show_log(self):
        print()
        with open(f"{self.name}.txt", 'r') as f:
            lines = f.readlines()
        for line in lines:
            print(line)
            
    # TODO: return wanted account
    @classmethod
    def return_account(cls, name):
        return cls.__accounts.get(name)

# TODO: put it in a while loop
while True:
    # TODO: for each action ask for user input
    account_req = input("1.Available account\n2.creating new account\n3.show accounts\n4.exit\nEnter intended number: ")
    try:
        account_req = float(account_req)
    except Exception:
        print("Invalid value")
    else:
        if account_req == 1:
            account_name = input('Enter name of your account: ')
            account = Banking.return_account(account_name)
            if account:
                password_input = input("Enter your password: ")
                if password_input == account.password:
                    while True:
                        operation = input("\n1.withdraw\n2.deposit\n3.show balance\n4.show log\n5.quit account\nEnter operation number: ")
                        try:
                            operation = float(operation)
                        except Exception:
                            print("Invalid value")
                        else:
                            if operation == 1:
                                amount = input("\nHow much do you wanna withdraw ? ")
                                try:
                                    amount = float(amount)
                                except:
                                    print("Invalid value")
                                else:
                                    account.withdraw(amount)
                            elif operation == 2:
                                amount = input("\nHow much do you wanna deposit ? ")
                                try:
                                    amount = float(amount)
                                except:
                                    print("Invalid value")
                                else:
                                    account.deposit(amount)
                            elif operation == 3:
                                account.show_balance()
                            elif operation == 4:
                                account.show_log()
                            elif operation == 5:
                                print("\n goodbye\n")
                                break
                            else:
                                print("Invalid value")
                else:
                    print("Password is not valid!!\n")    
            else:
                print("Account Not Found.")
                    
        elif account_req == 2:
            new_account_name = input("What's your new account name? ")
            new_account_password = input("Enter a password: (length must be more than 3)\n ")
            while len(new_account_password) < 3:
                new_account_password = input("Enter a password: (length must be more than 3)\n ")
            new_account = Banking(new_account_name, new_account_password)
        elif account_req == 3:
            Banking.show_accounts()
        elif account_req == 4:
            print("have a good day.")
            break
        else:
            print('Request is not valid.')