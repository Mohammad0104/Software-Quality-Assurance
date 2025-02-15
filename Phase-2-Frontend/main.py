import user
import login_logout 
import removeAccount
import createAccount


def handle_command(session):
    privlagedTransactions = ["create", "changeplan", "delete", "disable"]
    while session.logged_in:
        command = input("Enter a command (transaction/logout): ").strip().lower()
        
        if command == "logout":
            session.logout()
            break
        
        if command == "transaction":
            transaction = input("Enter transaction details: ").strip()
            
            if not transaction:
                print("Error: Please enter a transaction.")
                continue
            
            if not session.admin_mode and transaction in privlagedTransactions:
                print("pivileged transaction not allowed!")
                continue
            
            if transaction == "create" or transaction == "changeplan":
                t = createAccount.createAccount()
                run = getattr(t, transaction)
                session.transactions.append(run())
        
            elif transaction == "delete" or transaction == "disable":

                t = removeAccount.removeAccount()
                run = getattr(t, transaction)
                session.transactions.append(run())

            print(f"Transaction '{transaction}' completed successfully.")
        else:
            print("Invalid command. Please enter 'transaction' or 'logout'.")

            
def main():
    session = login_logout.Login()
    handle_command(session)
  

if __name__ == "__main__":
    main()
    
    
    
    # Old Code
# def login(users):
#     """Function to log in an existing user."""
#     user_id = input("Enter User ID: ")
#     password = input("Enter Password: ")
    
#     for usr in users:
#         if usr.user_id == user_id and usr.authenticate(password):
#             print("Authentication successful. Welcome!")
#             return usr
#     print("Authentication failed. Invalid credentials.")
#     return None




  # users = []  

    # while True:
    #     print("\nMain Menu:")
    #     print("1. Create Account")
    #     print("2. Login to the Banking System")
    #     print("3. Exit")
        
    #     choice = input("Enter your choice: ")
        
    #     if choice == "1":
    #         new_user = user.create_account()
    #         users.append(new_user)
    #         print("User created successfully!")
    #     elif choice == "2":
    #         user_instance = login(users)
    #         if user_instance:
    #             login_logout.main()  
    #     elif choice == "3":
    #         print("Exiting... Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Try again.")