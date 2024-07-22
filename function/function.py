# def add(x,y):
#     print( x + y)
# add(10,2)

# def sub(x,y):
#     print(x - y)
# sub(10,2)

# def mul(x,y):
#     print(x * y)
# add(2,2)

# def div(x,y):
#     print(x / y)
# sub(10,5)


# total = 10000
# def check_pin():
#     pin = int(input("Enter your PIN: "))
#     if pin == 1234:
#         print("Welcome user.")
#         return True
#     print("Wrong pin.")
#     return False

# def withdraw(total, amount):
#     total -= amount
#     return total

# def deposit(total,amount):
#     total += amount
#     return total

# def balance_inquiry(total):
#     return total

# def main():
#     global total
#     print("ATM")
#     print("Enter pin: ")
#     if check_pin():
#         while True:
#             choice = input("Enter your choice 'withdraw' or 'deposit' or 'balance_inquiry' or 'stop': ").lower()
#             if choice == "withdraw":
#                 amount = int(input("Enter the amount you want to withdraw: "))
#                 total = withdraw(total, amount)
#                 print(f"New balance: {total}")
#             elif choice == 'balance_inquiry':
#                 print(f"Your total is {balance_inquiry(total)}")
#             elif choice == "deposit":
#                 amount = int(input("Enter the amount you want to deposit: "))
#                 total = deposit(total,amount)
#                 print(f"New balance: {total}")
#             elif choice == "stop":
#                 print("Program stopped.")
#                 break
#             else:
#                 print("Enter correct option.")
#     else:
#         print("Access denied!")

# main()




# def total_marks(a,b,c,d,e):
#     total = int(a + b + c + d + e)
#     return total

# def student_percentage(total):
#     percentage = (total / 500) * 100
#     return percentage

# def grade(percentage):
#     if percentage > 75 and percentage <= 100:
#         return "Your grade is A"
#     elif percentage > 60 and percentage <= 75:
#         return "Your grade is B"
#     elif percentage > 45 and percentage <= 60:
#         return "Your grade is C"
#     elif percentage > 35 and percentage <= 45:
#         return "Your grade is D"
#     else:
#         return "Fail"

# def main():
#     print("Enter the marks of 5 subject :")
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     e = int(input())
#     total = total_marks(a,b,c,d,e)
#     print(f"Your total is {total}")
#     percentage = student_percentage(total)
#     print(f"Your percentage is {percentage}")
#     grade_result = grade(percentage)
#     print(f"Grade : {grade_result}")

# main()


# ecommerce
# productData = [
#     {'id':1,'name':'laptop', 'quantity':10,'price':50000},
#     {'id':2,'name':'mobile', 'quantity':20,'price':20000},
#     {'id':3,'name':'tablet', 'quantity':30,'price':10000},
#     {'id':4,'name':'desktop', 'quantity':40,'price':40000},
# ]

# # Displaying Products
# def display_product():
#     for product in productData:
#         print("Product id:",product['id'],"\t","Product name:",product['name'],"\t","Product quantity:",product['quantity'],"\t","Product price:",product['price'])

# def product_name(product_name):
#     for product in productData:
#         if product['name'] == product_name:
#             return product
#     return None

# def is_quantity_available(product, product_quantity):
#     return product_quantity <= product['quantity']

# def total(product_quantity, product):
#     return product_quantity * product['price'] 

# # Taking input from user for Product name and Quantity
# def main():
#     display_product()
#     name = input("Enter Product name: ")
#     quantity = int(input("Enter Product quantity: "))
#     product = product_name(name)
#     if product:
#         if is_quantity_available(product, quantity):
#             total_price = total(quantity, product)
#             print("Product name:", product['name'])
#             print("Product quantity:", quantity)
#             print("Total =", total_price)
#         else:
#             print("Entered quantity is not available.")
#     else:
#         print("Product not found.")

# main()


#*args
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(2,4,3))

# def mul(*args):
#     mul= 1
#     for i in args:
#         mul *= i
#     return mul
# print(mul(10, 2, 3))
