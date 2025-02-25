import user
import login_logout 
import removeAccount
import createAccount
import moveMoney

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
                
            elif transaction == "paybill":
                move_money = moveMoney.moveMoney()
                move_money.paybill()
                
            elif transaction == "transfer":
                move_money = moveMoney.moveMoney()
                move_money.transfer()
                
            elif transaction =="deposit":
                move_money = moveMoney.moveMoney()
                move_money.deposit()



            print(f"Transaction '{transaction}' completed successfully.")
        else:
            print("Invalid command. Please enter 'transaction' or 'logout'.")

            
def main():
    session = login_logout.Login()
    handle_command(session)
  

if __name__ == "__main__":
    main()
    
    
