# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import validation
import database
from getpass import getpass
#dictionary = {'user_details':['Haruna','Ibrahim','haarooun@gmail.com','looking', 5000]}


def init():
    print("Welcome to Himmscomp Bank")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);
        print(user)

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation(user)
    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):     
    print("**************withdrawal**************")
    try: 
        selected_option = int(input("What would you like to do? (1) Check Balance (2) Withdraw (3) Logout \n"))
        # get current balance
        if selected_option == 1:
            print("Your current balance is: ",get_current_balance(user))
            bank_operation(user)
        elif selected_option == 2:
            amount = int(input("Enter Amount to be withdrawn\n"))
            if int(get_current_balance(user))> int(amount):
                balance= int(get_current_balance(user))- int(amount)
                print("Your Balance is", balance)
            else:
                ("You have insufficient Balance")
        elif selected_option == 3:
            login()
             
    except:
            print("an Invalid input, Enter a number")
    # get amount to withdraw
    
        
    # check if current balance > withdraw balance
    
    # deduct withdrawn amount form current balance
    
    # display current balance
    
    


def deposit_operation(user):
    print("**********Deposit Operations***********")
    try: 
        selected_option = int(input("What would you like to do? (1) Check Balance (2) Deposit (3) Logout \n"))
        # get current balance
        if selected_option == 1:
            print("Your current balance is: ",get_current_balance(user))
            bank_operation(user)
            
    # get amount to deposit
        elif selected_option == 2:
            balance = int(input("Enter Amount to be deposited\n"))
            balance = str(int(user[4]) + balance)
            print("Your Current Balance is :", balance)
    
        # add deposited amount to current balance
        # display current balance
        elif selected_option == 3:
            login()
    except:
        print("an Invalid input, Enter a number")

def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user, balance):
    user[4] = balance


def get_current_balance(user):
    return user[4]


def logout():
    login()


init()
