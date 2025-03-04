import user
import login_logout 
import removeAccount
import createAccount
import moveMoney

def handle_command(session):
    privlagedTransactions = ["create", "changeplan", "delete", "disable"]
    while session.logged_in:
        transaction = input("").strip().lower()
        
        if transaction == "logout":
            session.logout()
            break
        
        if not transaction:
            print("Error: Please enter a transaction.")
            continue
            
        if not session.admin_mode and transaction in privlagedTransactions:
            print("pivileged transaction not allowed!")
            continue
            
        if transaction == "create" or transaction == "change_plan":
            t = createAccount.createAccount()
            run = getattr(t, transaction)
            session.transactions.append(run())
        
        elif transaction == "delete" or transaction == "disable":
            t = removeAccount.removeAccount()
            run = getattr(t, transaction)
            session.transactions.append(run())
                
        elif transaction == "pay_bill":
            move_money = moveMoney.moveMoney()
            move_money.pay_bill()
                
        elif transaction == "transfer":
            move_money = moveMoney.moveMoney()
            move_money.transfer()
                
        elif transaction =="deposit":
            move_money = moveMoney.moveMoney()
            move_money.deposit()

        else:
            print("Error: Please enter a transaction.")

            
def main():
    logging_in = input("").strip().lower()
    if logging_in == "login":
        session = login_logout.Login()
        handle_command(session)
  

if __name__ == "__main__":
    main()
    
    
