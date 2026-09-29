# ATM project
import numpy
import math
import choice as ch

print("WELCOME TO ATM")

balance=100000
pin=6267



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
    ch.ch(choice,balance)
else:
    print("wrong PIN")

print("\nTHANK YOU ")
