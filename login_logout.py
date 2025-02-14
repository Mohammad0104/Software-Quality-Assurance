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

def main():
    logged_in = False
    admin_mode = False
    transactions = []
    
    while True:
        if not logged_in:
            print("\nLogin - Welcome to the banking system")
            session_type = input("Enter session type (Standard/Admin): ").strip().lower()
            
            if session_type not in ["standard", "admin"]:
                print("Invalid session type. Please enter 'Standard' or 'Admin'.")
                continue
            
            account_holder = ""
            if session_type == "standard":
                account_holder = input("Enter account holder's name: ").strip()
                if not account_holder:
                    print("Account holder's name is required for Standard login.")
                    continue
            
            # Read bank accounts file
            bank_accounts = read_bank_accounts()
            
            logged_in = True
            admin_mode = session_type == "admin"
            print(f"Login Successful: Welcome {account_holder if account_holder else 'Admin'} ({session_type.capitalize()})!")
            
        command = input("Enter a command (transaction/logout): ").strip().lower()
        
        if command == "logout":
            if not logged_in:
                print("Error: You are not logged in.")
                continue
            
            # Write transaction file before logout
            write_transactions(transactions)
            
            print("Logout Successful. Session ended.")
            logged_in = False
            admin_mode = False
            transactions.clear()
            continue
        
        if not logged_in:
            print("Error: No transaction is allowed before login.")
            continue
        
        if command == "transaction":
            transaction = input("Enter transaction details: ").strip()
            
            if not transaction:
                print("Error: Please enter a transaction.")
                continue
            
            if not admin_mode and transaction.lower() == "admin_only":
                print("Error: This transaction is only allowed for admin users.")
                continue
            
            print(f"Transaction '{transaction}' completed successfully.")
            transactions.append(transaction)
        else:
            print("Invalid command. Please enter 'transaction' or 'logout'.")

if __name__ == "__main__":
    main()
