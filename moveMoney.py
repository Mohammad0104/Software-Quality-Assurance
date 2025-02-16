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
        self.account_holder = input("Enter account holder: ")
        

        #User enters account number whom they want money transferred to/from
        self.transferTo = input("Enter account number to transfer to: ")
        self.transferFrom = input("Enter account number to transfer from: ")

        print(f"balance value: {self.balance}")

        #Checks if amount inputted is within limit
        while (not amountCheck):
            self.transferAmount = float(input("Enter amount to transfer: "))
            
            if (self.transferAmount > self.balance and self.transferAmount > 1000):
                print("Transfer amount is greater than Balance and is over $1000, try again!")
                transferAmount = 0.0
                amountCheck = False

            elif (self.transferAmount > self.balance or self.transferAmount > 1000):
                print("Try again!")
                transferAmount = 0.0
                amountCheck = False
            
            else:
                amountCheck = True

        print("Transfer payment has been completed!")




    def paybill(self):
        company = ''
        companyCheck = False
        payAmount = 0.0

        amountCheck = False

        #User enters account holder
        self.account_holder = input("Enter account holder: ")
        
        #User enters account number
        self.account_number = input("Enter account number: ")

        #Checks if company inputted is on the list
        while (not companyCheck):
            self.company = input("Enter either of these companies initials that will pay the bills (EC, CQ, or FI): ")

            if (self.company.upper() != "EC" and self.company.upper() != "CQ" and self.company.upper() != "FI"):
                print("Company initials is invalid, try again!")
                companyCheck = False

            else:
                companyCheck = True


        print(f"balance value: {self.balance}")

        #Checks if amount inputted is within limit
        while (not amountCheck):
            self.payAmount = float(input("Enter the amount to pay: "))
            
            if (self.payAmount > self.balance and self.payAmount > 2000):
                print("Amount paid is greater than Balance and is over $2000, try again!")
                payAmount = 0.0
                amountCheck = False

            elif (self.payAmount > self.balance or self.payAmount > 2000):
                print("Try again!")
                payAmount = 0.0
                amountCheck = False
            
            else:
                amountCheck = True

        print("Bill payment has been completed!")




    def deposit(self):

        depositAmount = 0.0

        #User enters account holder
        self.account_holder = input("Enter account holder: ")

        #User enters account number
        self.account_number = input("Enter account number: ")

        self.depositAmount = input("Enter amount to deposit: ")

        print("Deposit payment has been completed!")



account = moveMoney()
account.transfer()
account.paybill()
account.deposit()