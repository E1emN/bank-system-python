import random

is_start = True
is_logged_in = False
menu = 3
mii = 400000
ai = 0
checkcum = 7
user_card = 0
user_pin = 0
balance = 0

def convert(list): 
    s = [str(i) for i in list]   
    res = int("".join(s))  
    return(res)

def print_menu():
    global menu

    print(r"""
    1. Create an account
    2. Log into account
    0. Exit
    """)
    menu = int(input())

def create_account(): 
    global user_card, user_pin, menu, ai
    
    ai = random.randint(100000000, 999999999)
    user_pin = random.randint(1000, 9999)
    user_card = convert([mii, ai, checkcum])

    print("Your card number:")
    print(user_card)
    print("Your card PIN:")
    print(user_pin)

    menu = 0

def login():
    global menu, is_logged_in

    print("Enter your card number:")
    card = int(input())
    print("Enter your PIN:")
    pin = int(input())
    
    if (card == user_card and pin == user_pin):
       print("You have successfully logged in!")
       is_logged_in = True
    else:
        print("Wrong card number or PIN!") 
        print(user_card, user_pin)
        menu = 0

def exit():
    global is_start
    print("Bye!")
    is_start = False

def print_user_menu():
    global menu

    print(r"""
    1. Balance
    2. Log out
    0. Exit
    """)

    menu = int(input())

def show_balance():
    print(f"Balance: {balance}")

def logout():
    global is_logged_in
    is_logged_in = False

while is_start:
    if is_logged_in == False:
        print_menu()
        if menu == 1:
            create_account()
        elif menu == 2:
            login()
        elif menu == 0:
            exit()
    else:
        print_user_menu()
        if menu == 1:
            show_balance()
        elif menu == 2:
            logout()
        elif menu == 0:
            exit()