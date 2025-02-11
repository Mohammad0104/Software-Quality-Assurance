import user
import login_logout

def login(users):
    """Function to log in an existing user."""
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    
    for usr in users:
        if usr.user_id == user_id and usr.authenticate(password):
            print("Authentication successful. Welcome!")
            return usr
    print("Authentication failed. Invalid credentials.")
    return None

def main():
    users = []  
    
    while True:
        print("\nMain Menu:")
        print("1. Create Account")
        print("2. Login to the Banking System")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_user = user.create_account()
            users.append(new_user)
            print("User created successfully!")
        elif choice == "2":
            user_instance = login(users)
            if user_instance:
                login_logout.main()  
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
