import user
import login_logout

def main():
    users = []  # Store created users
    
    while True:
        print("\nMain Menu:")
        print("1. Create Account")
        print("2. Login and Logout to the Banking System")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_user = user.create_account()
            users.append(new_user)
            print("User created successfully!")
        elif choice == "2":
            print("\nLogin - Start a Banking Session")
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
            
            user_instance = user.login(users)
            if user_instance:
                login_logout.banking_terminal()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
