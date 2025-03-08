class CreateAccount:
    def __init__(self, account_file='accounts.txt'):
        # Initialize with a specified account file and calculate the next account number.
        self.account_file = account_file
        self.next_account_number = self.get_next_account_number()

    def get_next_account_number(self):
        """Retrieve the next account number by reading the last entry in the account file."""
        try:
            with open(self.account_file, 'r') as file:
                lines = file.readlines()
                
                if lines:
                    last_line = lines[-1].strip()
                    last_account_line = lines[-2] if last_line == 'END_OF_FILE' else last_line
                    return int(last_account_line.split()[0]) + 1
                else:
                    return 1  
        except FileNotFoundError:
            return 1  

    def create(self):
        """Create a new bank account by prompting the user for account details and appending to the account file."""
        account_holder = input("Enter account holder: ").ljust(20)
        initial_balance = float(input("Enter an initial balance: "))  
        formatted_balance = f"{initial_balance:08.1f}"  

        account_number = str(self.next_account_number).zfill(5)  
        account_info = f"{account_number} {account_holder} A {formatted_balance}"  

        
        with open(self.account_file, 'r+') as file:
            lines = file.readlines()
            if lines and lines[-1].strip() == 'END_OF_FILE':
                lines = lines[:-1]  

            file.seek(0)  
            file.writelines(lines)  
            file.truncate()  
            
            file.write(account_info + '\n') 
            file.write("END_OF_FILE\n")  

        #  account created successfully 
        print(f'Account {account_number} was created with initial balance {formatted_balance}')
        self.next_account_number += 1  
        return account_info

#create a new account
account_create = CreateAccount()
account_create.create()
