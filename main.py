# ATM project

from datetime import datetime
import choice as ch

print("WELCOME TO ATM")

balance=100000
pin=6267

transtime=datetime.now()

print(transtime)

user_pin=int(input("enter your atm pin:"))
if user_pin==pin:
    while True:
        
        print("hello customer")

        print("Menu")
        print("1-Check balance")
        print("2-Deposit Money")
        print("3-withdraw Money")
        print("4-transaction analysis")
        print("5-exit")

        choice=int(input("enter you choice:-"))
        balance=ch.ch(choice,balance)
        if choice==5:
            break
else:
    print("wrong PIN")

print("\nTHANK YOU ")
