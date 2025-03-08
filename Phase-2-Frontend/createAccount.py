class CreateAccount:
    def __init__(self, account_file='accounts.txt'):
        """Initialize the class with the path to the accounts file and set the next account number."""
        self.account_file = account_file
        self.next_account_number = self.get_next_account_number()

    def get_next_account_number(self):
        """Determines the next account number by reading the last entry in the accounts file."""
        try:
            with open(self.account_file, 'r') as file:
                lines = file.readlines()
                if lines and lines[-1].startswith('END_OF_FILE'):
                    last_account_number = int(lines[-2].split()[0])
                else:
                    last_account_number = int(lines[-1].split()[0]) if lines else 0
                return last_account_number + 1
        except FileNotFoundError:
            return 1

    def create(self):
        """Prompts user input for account details, creates a new account, and appends it to the accounts file."""
        account_holder = input("Enter account holder: ").ljust(20)
        initial_balance = input("Enter an initial balance: ").zfill(8)
        account_number = str(self.next_account_number).zfill(5)
        account_info = f"{account_number} {account_holder} A {initial_balance}"

        with open(self.account_file, 'a') as file:
            file.write(account_info + '\n')

        print(f'Account {account_number} was created with initial balance {initial_balance}')
        self.next_account_number += 1  
        return account_info

# Create an instance and add a new account
createAccount = CreateAccount()
createAccount.create()
