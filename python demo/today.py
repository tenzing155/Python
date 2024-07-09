# x = 10
# y = 20
# if x > y:
#     print("x is greater than y")
# elif x == 0:
#     print("x and y are equal")
# else:
#     print("x is greater than x")


# age = int(input("Enter your age :"))
# if age >= 18:
#     if age >= 18 and age <= 60:
#         print("You are eligible to vote.")
#     else:
#         print("You are old")
# else:
#     print("You are a child")

print("ATM")
print("Enter your pin.")
pin = int(input())
if pin == 1234:
    print("Welcome user.")
    print("withdraw or  balance inquiry")
    w = input()
    total = 10000
    if w == "withdraw":
        print(f"Your total amount is {total}")
        print(f"Enter the amount you want to withdraw.")
        amount = int(input())
        bal = total - amount
        print(f"Your balance is {bal}")
    elif w == "balance inquiry":
        print(f"Your total is {total}")
else :
    print("Pin did not match")
    
    

