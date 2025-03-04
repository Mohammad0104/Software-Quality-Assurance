class moveMoney:
    account_holder = ''
    account_number = 0
    balance = 1000.00
    
    
    def transfer(self):
        transferTo = 0
        transferFrom = 0
        transferAmount = 0.0

        amountCheck = False
    
        #User enters account holder
        self.account_holder = input("Enter account holder ")
        

        #User enters account number whom they want money transferred to/from
        self.transferTo = input("enter account number to transfer to ")
        self.transferFrom = input("enter account number to transfer from ")

        print(f"balance value: {self.balance}")

        #Checks if amount inputted is within limit
        while (not amountCheck):
            self.transferAmount = float(input("enter amount to transfer "))
            
            if (self.transferAmount > self.balance and self.transferAmount > 1000):
                print("transferred failed! Please enter transfer value less than 1000")
                transferAmount = 0.0
                amountCheck = False

            elif (self.transferAmount > self.balance or self.transferAmount > 1000):
                print("Try again!")
                transferAmount = 0.0
                amountCheck = False
            
            else:
                amountCheck = True

        print("Transfer accepted")




    def pay_bill(self):
        company = ''
        companyCheck = False
        payAmount = 0

        amountCheck = False

        #User enters account holder
        self.account_holder = input("Enter account holder ")
        
        #User enters account number
        self.account_number = input("Enter account number ")

        #Checks if company inputted is on the list
        while (not companyCheck):
            self.company = input("enter company: ")

            if (self.company.upper() != "EC" and self.company.upper() != "CQ" and self.company.upper() != "FI"):
                print("Company initials is invalid, try again!")
                companyCheck = False

            else:
                companyCheck = True


        # print(f"balance value: {self.balance}")

        #Checks if amount inputted is within limit
        while (not amountCheck):
            self.payAmount = int(input("enter bill "))
            
            if (self.payAmount > self.balance and self.payAmount > 2000):
                print("Bill input is over 2000, it must be less than that!")
                payAmount = 0
                amountCheck = False

            elif (self.payAmount > self.balance or self.payAmount > 2000):
                print("Try again!")
                payAmount = 0
                amountCheck = False
            
            else:
                amountCheck = True

        print(f'{self.payAmount} bill sent to account {self.account_number}')




    def deposit(self):

        depositAmount = 0.0

        #User enters account holder
        self.account_holder = input("enter account holder ")

        #User enters account number
        self.account_number = input("enter account number ")

        self.depositAmount = input("enter amount to deposit ")

        print(f'{self.depositAmount} deposited into account {self.account_number}')
