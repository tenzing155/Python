# total = 10000
# withdraw - 2000 max
# deposit - 1000 max
# check_balance


# def withdraw(total,withdraw_amount):
#     if withdraw_amount < 5000:
#         total -= withdraw_amount
#         print(f"Amount withdrawn : {withdraw_amount}")
#         return total
#     else:
#         print("Max amount exceeded!")

# def deposit(total,deposit_amount):
#     if deposit_amount < 5000:
#         total += deposit_amount
#         print(f"Amount deposited : {deposit_amount}")
#         return total
#     else:
#         print("Max amount exceeded!")

# def check_balance(total):
#     print(f"Your total balance is {total}")


# def main():
#     total = 10000
#     while True:
#         print("=========BANK=========")
#         operation = input("Enter the operation. (withdraw, deposit, check_balance) or 'stop' the program: ")
#         if operation == "withdraw":
#             withdraw_amount = int(input("Amount to withdraw: "))
#             total =  withdraw(total,withdraw_amount)
#         elif operation == "deposit":
#             deposit_amount = int(input("Amount to be deposited: "))
#             total = deposit(total,deposit_amount)  
#         elif operation == "check_balance":
#             total = check_balance(total)
#         elif operation == "stop":
#             print("Progran stopped.")
#             break
#         else:
#             print("Invalid operation. Please try again.")

# main()
