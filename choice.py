import numpy as np
transaction=[]
def ch(choice,balance):
    
    if choice==1:
        print("your balance is:-",balance)
    elif choice==2:
        print("miminum deposit amount is 100")
        deposit=float(input("enter deposit amount:-"))
        if deposit>=100:
            balance=balance+deposit
            transaction.append(+deposit)
            print("Amount deposit sucesssfully")
            print("account balance is:-",balance)
        else:
            print("invalaid amount ")
            print("please deposit more then 100 RS")

    elif choice==3:
        print("minimum withdraw amount is 100Rs")
        amount=int(input("enter withdraw amount:- "))
        if amount<100:
            print("Invalid amount")
        elif amount<=balance:
            balance=balance-amount
            transaction.append(-amount)
            print("amount withdraw sucessfully  collect your amount")
            print("account balance is:-",balance)
        else:
            print("insufficient balance")

    elif choice==4:
        
        if len(transaction)==0:
        
            print("no transaction histry")
        else:
            transaction_array=np.array(transaction)
            print("transaction analysis")
            print("total transaction :",len(transaction_array))
            print("total transaction amount:",np.sum(transaction_array))
            print("largest transaction :",np.max(transaction_array))
            print("Smallest transaction :",np.min(transaction_array))
            print("Average tramsaction :",np.mean(transaction_array))
    elif choice==5:
        print("THANK YOU for using ATM")
    else:
        print("wrong menu")
    return balance
