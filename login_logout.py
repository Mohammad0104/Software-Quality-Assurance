import sys

def read_bank_accounts():
    """Simulates reading the current bank accounts file."""
    print("Reading bank accounts file...")
    return {}

def write_transactions(transactions):
    """Simulates writing the transaction log to a file."""
    print("Writing transactions to file...")
    for transaction in transactions:
        print(transaction)

class Login:
    
    def __init__(self):
        self.logged_in = False
        self.admin_mode = False
        self.account_holder = ""
        self.transactions = []
        self.start_session()
    
    def start_session(self):
        while not self.logged_in:
            print("\nLogin - Welcome to the banking system")
            session_type = input("Enter session type (Standard/Admin): ").strip().lower()
            
            if session_type not in ["standard", "admin"]:
                print("Invalid session type. Please enter 'Standard' or 'Admin'.")
                continue
            
            if session_type == "standard":
                self.account_holder = input("Enter account holder's name: ").strip()
                if not self.account_holder:
                    print("Account holder's name is required for Standard login.")
                    continue
            
            
            self.bank_accounts = read_bank_accounts()
            
            self.logged_in = True
            self.admin_mode = session_type == "admin"
            print(f"Login Successful: Welcome {self.account_holder if self.account_holder else 'Admin'} ({session_type.capitalize()})!")
    
    def logout(self):
        if not self.logged_in:
            print("Error: You are not logged in.")
            return
        
        
        write_transactions(self.transactions)
        
        print("Logout Successful. Session ended.")
        self.logged_in = False
        self.admin_mode = False
        self.account_holder = ""
        self.transactions.clear()
   
