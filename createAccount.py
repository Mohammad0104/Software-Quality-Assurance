nextAccount = 0

class createAccount:
    accountHolder = ''
    accountNumber = ''
    initialBalance = 0
    paymentPlan = 'SP'
    transactionFileLine = ''
    accountInfo = ''

    def create(self):
        global nextAccount

        self.accountHolder = input("enter account holder ").ljust(20)
        self.initialBalance = input("enter an initial balance ").zfill(8)
        nextAccount += 1
        self.accountNumber = str(nextAccount).zfill(5)

        self.transactionFileLine = "05 " + self.accountHolder + " " + self.accountNumber + " " + self.initialBalance+ " AA"
        self.accountInfo = self.accountNumber + ' ' + self.accountHolder + ' A ' + self.initialBalance


        #add to current account file
        #add transaction line to file
        print(f'account {self.accountNumber} was created with initial balance {self.initialBalance}')
        return self.transactionFileLine

    def changeplan(self):
        self.accountHolder = input("enter account holder ")
        self.accountNumber = input("enter account number ")
        self.paymentPlan = 'NP'

        #get balance from account file
        #update to current account file
        #add transaction line to file
        self.transactionFileLine = "08 " + str(self.accountHolder).ljust(20) + " " + self.accountNumber + " " + str(self.initialBalance).zfill(8) + " " + self.paymentPlan
        self.accountInfo = self.accountNumber + ' ' + self.accountHolder + ' A ' + str(self.initialBalance)
        
        print(f'account {self.accountNumber} payment plan changed to non-student')
        return self.transactionFileLine


# p1 = createAccount()
# # p1.createAccount()
# p1.changePlan()