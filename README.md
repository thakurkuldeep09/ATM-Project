# ATM-Project
A simple Python ATM project lets users check their balance, deposit money, withdraw money, transition,and exit
# ATM project
import numpy as np

print("WELCOME TO ATM")

balance=100000
pin=6267

transaction=[]

user_pin=int(input("enter your atm pin:"))
if user_pin==pin:
    print("hello customer")

    print("Menu")
    print("1-Check balance")
    print("2-Deposit Money")
    print("3-withdraw Money")
    print("4-transaction analysis")
    print("5-exit")

    choice=int(input("enter you choice:-"))

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
            print("total transaction amount:",np.sum(ransaction_array))
            print("largest transaction :",np.max(transaction_array))
            print("Smallest transaction :",np.min(transaction_array))
            print("Average tramsaction :",np.mean(transaction_array))
    elif choice==5:
        print("THANK YOU for using ATM")
    else:
        print("wrong menu")
else:
    print("wrong PIN")

print("\nTHANK YOU ")
