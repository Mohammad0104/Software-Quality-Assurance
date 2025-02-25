class removeAccount:
    account_holder = ''
    account_number = ''
    balance = 500 
    active = True
    transaction_file_line = ''


    def delete(self):
        self.account_holder = input("enter account holder ")
        self.account_number = input("enter account number ")

        #remove from current account file
        self.transaction_file_line = "06 " + str(self.account_holder).ljust(20) + " " + self.account_number + " " + str(self.balance).zfill(8) + " DD"
        print(f'account {self.account_number} was deleted')

        return self.transaction_file_line

    def disable(self):
        self.account_holder = input("enter account holder ")
        self.account_number = input("enter account number ")
        self.active = False

        #update current account file
        #add transaction line to file
        self.transaction_file_line = "07 " + str(self.account_holder).ljust(20) + " " + self.account_number + " " + str(self.balance).zfill(8) + " DD" 
        print(f'account {self.account_number} was disabled')

        return self.transaction_file_line

