next_account = 0

class createAccount:
    account_holder = ''
    account_number = ''
    initial_balance = 0
    payment_plan = 'SP'
    transaction_file_line = ''
    account_info = ''

    def create(self):
        global next_account

        self.account_holder = input("enter account holder ").ljust(20)
        self.initial_balance = input("enter an initial balance ").zfill(8)
        next_account += 1
        self.account_number = str(next_account).zfill(5)

        self.transaction_file_line = "05 " + self.account_holder + " " + self.account_number + " " + self.initial_balance+ " AA"
        self.account_info = self.account_number + ' ' + self.account_holder + ' A ' + self.initial_balance


        #add to current account file
        #add transaction line to file
        print(f'account {self.account_number} was created with initial balance {self.initial_balance}')
        return self.transaction_file_line

    def changeplan(self):
        self.account_holder = input("enter account holder ")
        self.account_number = input("enter account number ")
        self.payment_plan = 'NP'

        #get balance from account file
        #update to current account file
        #add transaction line to file
        self.transaction_file_line = "08 " + str(self.account_holder).ljust(20) + " " + self.account_number + " " + str(self.initial_balance).zfill(8) + " " + self.payment_plan
        self.account_info = self.account_number + ' ' + self.account_holder + ' A ' + str(self.initial_balance)
        
        print(f'account {self.account_number} payment plan changed to non-student')
        return self.transaction_file_line
