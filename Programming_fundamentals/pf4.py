# a program that simulates a basic ATM system with withdrawals and deposits
account = {}
def welcome():
    return """
        ***Hey! Welcome to BlingBank 😎 The bank made by you for you.***
        What operation are you going to do today ?

        1 - Create an account
        2 - Make a Withdrawal
        3 - Make a deposit
        4 - Check your account status
        5 - Delete your bank account and leave our bank
        """

def create_account(name):
    account[name] = 1000
    return f"Well done! Your account is created."

def delete_account(name):
    del account[name]
    return f"What a pity! {name} account is delete."

def withdrawal(name):
    amount = int(input("Amount of withdrawal: "))
    if account[name] < amount:
        return f"You can't do that withdrawal"
    else:
        account[name] = account[name] - amount
        return f"You retired {amount} from your bank account. You current sold is {account[name]}"

def deposit(name):
    amount = int(input("Amount of deposit: "))
    account[name] = account[name] + amount
    return f"You put {amount} in your bank account. You current sold is {account[name]}"

def account_status(name):
    return f"Your current sold is {account[name]} dollars"


def bank_manager():
    print(welcome())

    while True:
        choice = input("Enter operation number (1-5) or 'q' to quit: ")
        
        if choice == 'q':
            print("Exiting Bank. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5'):
            print("Invalid input. Please try again.")
            continue
        
        name = input("Please enter your name: ")

        if choice == '1':
             print(create_account(name))
        elif choice == '2':
            print(withdrawal(name))
        elif choice == '3':
            print(deposit(name))
        elif choice == '4':
            print(account_status(name))
        elif choice == '5':
            print(delete_account(name))
        
        print()



bank_manager()