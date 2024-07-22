# total = 10000
# withdraw - 2000 max
# deposit - 1000 max
# check_balance

total = 10000

while True:
    print("=========BANK=========")
    operation = input("Enter the operation. (withdraw, deposit, check_balance): ")
    if operation == "withdraw":
        withdraw_amount = int(input("Amount to withdraw: "))
        if withdraw_amount > 2000:
            print("Only max of 2000 is allowed.")
        else:
            total -= withdraw_amount
            print(f"Amount withdrawn {withdraw_amount}")
    elif operation == "deposit":
        deposit_amount = int(input("Amount to be deposited: "))
        if deposit_amount > 1000:
            print("Only max of 2000 is allowed.")
        else:
            total += deposit_amount 
            print(f"Amount deposited {deposit_amount}") 
    elif operation == "check_balance":
        balance = total
        print(f"Your total balance is {balance}")
    elif operation == "stop":
        print("Program stopped.")
        break
    else:
            print("Invalid operation. Please try again.")


