class removeAccount:
    accountHolder = ''
    accountNumber = ''
    active = True
    transactionFileLine = ''
    balance = 500 #get balance from account file


    def delete(self):
        self.accountHolder = input("enter account holder ")
        self.accountNumber = input("enter account number ")

        #remove from current account file
        self.transactionFileLine = "06 " + str(self.accountHolder).ljust(20) + " " + self.accountNumber + " " + str(self.balance).zfill(8) + " DD"
        print(f'account {self.accountNumber} was deleted')

        return self.transactionFileLine

    def disable(self):
        self.accountHolder = input("enter account holder ")
        self.accountNumber = input("enter account number ")
        self.active = False

        #update current account file
        #add transaction line to file
        self.transactionFileLine = "07 " + str(self.accountHolder).ljust(20) + " " + self.accountNumber + " " + str(self.balance).zfill(8) + " DD" 
        print(f'account {self.accountNumber} was disabled')

        return self.transactionFileLine

    
# p1 = removeAccount()
# p1.deleteAccount()
# p1.disableAccount()

