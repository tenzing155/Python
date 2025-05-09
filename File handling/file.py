#files -
# bin   txt
# w r a

#reading file
# f = open("file name", "r")    
# text = f.read()
# print(text)

#writing file
# f = open("filename", "w")
# f.write("contents\n")
# f.close()

#alternative
# with open("filename","something") as file:
#     file.write("contents\n")



#write files: 
#name,email,phone,address
# obj = open("file.txt","w")
# name = input("Enter your name: ")
# email = input("Enter your email: ")
# phone = input("Enter your phone number: ")
# address = input("Enter your address: ")

# obj.write(f"name: {name}\n")
# obj.write(f"email: {email}\n")
# obj.write(f"phone: {phone}\n")
# obj.write(f"address: {address}\n")

# read files:
# obj = open("file.txt","r")
# print(obj.read())


# marks of 5 subjects and store in a file
# obj = open("marks.txt","w")
# english = int(input("Enter marks of english: "))
# math = int(input("Enter marks of math: "))
# science = int(input("Enter marks of science: "))
# nepali = int(input("Enter marks of nepali: "))
# computer = int(input("Enter marks of computer: "))
# total = english + math + science + nepali + computer
# percentage = (total / 500) * 100
# if percentage > 75 and percentage <= 100:
#     grade = "A"
# elif percentage > 60 and percentage <= 75:
#     grade = "B"
# elif percentage > 45 and percentage <= 60:
#     grade = "C"
# elif percentage > 35 and percentage <= 45:
#     grade = "D"
# else:
#     grade = "F"

# obj.write(f"Total marks is {total} \n") 
# obj.write(f"Percentage is {percentage} \n")
# obj.write(f"Your grade is {grade}")

# read file
# obj = open("file.txt","r")
# print(obj.read())


# with open("marks.txt", "a") as obj:
#     while True:
#         option = input("Start or Stop: ").lower()
#         if option == "start":
#             while True:
#                 name = input("Enter the student's name: ")
#                 english = int(input("Enter marks of English: "))
#                 math = int(input("Enter marks of Math: "))
#                 science = int(input("Enter marks of Science: "))
#                 nepali = int(input("Enter marks of Nepali: "))
#                 computer = int(input("Enter marks of Computer: "))
#                 total = english + math + science + nepali + computer
#                 percentage = (total / 500) * 100
                
#                 if percentage > 75 and percentage <= 100:
#                     grade = "A"
#                 elif percentage > 60 and percentage <= 75:
#                     grade = "B"
#                 elif percentage > 45 and percentage <= 60:
#                     grade = "C"
#                 elif percentage > 35 and percentage <= 45:
#                     grade = "D"
#                 else:
#                     grade = "F"
                
#                 obj.write(f"Student Name: {name}\n")
#                 obj.write(f"Total marks: {total}\n")
#                 obj.write(f"Percentage: {percentage:.2f}%\n")
#                 obj.write(f"Grade: {grade}\n")
#                 obj.write("\n")  
                
#                 continue_option = input("Do you want to continue? (yes/no): ").lower()
#                 if continue_option != 'yes':
#                     print("Program stopped.")
#                     break
#                 else:
#                     print("Program continued.")
#             break
#         elif option == "stop":
#             print("Program stopped.")
#             break
#         else:
#             print("Invalid option, please enter 'Start' or 'Stop'.")


# with open("computerbazaar.txt", "a") as file:
#     while True:
#         print("=============Computer Bazar============")
#         name = input("Enter your name: ")
        
#         if not name.isalpha():
#             print("Only letters are allowed.")
#             continue

#         print("1.Dell(Rs.20000) 2.Toshiba(Rs.30000) 3.Mac(Rs.500000)")
#         dell_price = 0
#         toshiba_price = 0
#         mac_price = 0
#         product_name = ""
#         quantity = 0

#         option = int(input("Enter the option: "))

#         if option == 1:
#             quantity = int(input("Enter the quantity: "))
#             dell_price = 20000 * quantity
#             product_name = "Dell"
#         elif option == 2:
#             quantity = int(input("Enter the quantity: "))
#             toshiba_price = 30000 * quantity
#             product_name = "Toshiba"
#         elif option == 3:
#             quantity = int(input("Enter the quantity: "))
#             mac_price = 500000 * quantity
#             product_name = "Mac"
#         else:
#             print("Invalid option")
#             continue 

#         print("Delivery option: 1.Home Delivery(Rs.1000) 2.Pick up(free)")
#         delivery_option = int(input("Enter the delivery option: "))
#         delivery_price = 0
#         if delivery_option == 1:
#             delivery_price = 1000

#         print("Packing: 1. Plastic bag(Rs.1000) 2. Bag(Rs.2000) 3. Gift Box(Rs.5000)")
#         packing_option = int(input("Enter the packing option: "))
#         packing_price = 0
#         if packing_option == 1:
#             packing_price = 1000
#         elif packing_option == 2:
#             packing_price = 2000
#         elif packing_option == 3:
#             packing_price = 5000

#         total = dell_price + toshiba_price + mac_price
#         tax_amount = 0
#         print("Location: 1.KTM(Rs:13% tax) 2.Lalitpur(Rs:0% tax) 3.Bhaktapur(Rs:10% tax)")
#         tax_option = int(input("Enter the tax option: "))
#         if tax_option == 1:
#             tax_amount = total * 0.13
#         elif tax_option == 2:
#             tax_amount = 0
#         elif tax_option == 3:
#             tax_amount = total * 0.1

#         grand_total = total + delivery_price + packing_price + tax_amount
#         print("Your records have been saved!")

#         file.write("============COMPUTER BAZAAR=============\n")
#         file.write(f"Customer name: {name}\n")
#         file.write(f"Product name: {product_name}\n")
#         file.write(f"Quantity: {quantity}\n")
#         file.write(f"Total: {total}\n")
#         file.write(f"Delivery Price: {delivery_price}\n")
#         file.write(f"Packing Price: {packing_price}\n")  
#         file.write(f"Tax amount: {tax_amount}\n")
#         file.write(f"Grand Total: {grand_total}\n")
#         file.write("\n")  # Add a new line for better readability between records

#         continue_option = input("Do you want to continue? (yes/no): ").lower()
#         if continue_option != 'yes':
#             print("Program stopped.")
#             break
#         else:
#             print("Program continued.")

    

# import os

# if not os.path.exists("users.txt"):
#     handle = open("users.txt", "w")
#     handle.close()

# def register():
#     print("=============Register User==============")
#     username = input("Enter your username:").strip()
#     with open("users.txt", "r") as file:
#         handle = file.read()
#         if username in handle:
#             print("Username already exists.")
#             exit()
    
#     password = input("Enter password: ").strip()
#     confirm_password = input("Confirm password: ").strip()
    
#     if password != confirm_password:
#         print("Passwords do not match")
#         exit()
    
#     with open("users.txt", "a") as file:
#         file.write(f"username:{username},password:{password}\n")
#         print("User registered successfully")

# def login():
#     print("================Login User=============")
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ").strip()
#     with open("users.txt", "r") as file:
#         users = file.readlines()
#         is_login = False
#         for user in users:
#             user = user.strip().split(",")
#             uname = user[0].split(":")[1]
#             upass = user[1].split(":")[1]
#             if username == uname and password == upass:
#                 is_login = True
    
#         if is_login:
#             print("Login successful.")
#         else:
#             print("Invalid credentials.")

# register()
# login()


#name quantity total 
# with open("products.txt", "a") as file:
#     while True:
#         name = input("Enter your name: ")
        
#         if not name.isalpha():
#             print("Only letters are allowed.")
#             continue

#         print("MENU:")
#         print(" 1.Apple: Rs200\n 2.Banana: Rs120\n 3.Mango: Rs130\n 4.Strawberries: Rs150\n 5.Litchi: Rs140\n")
#         apple_price = 0
#         banana_price = 0
#         mango_price = 0
#         strawberries_price = 0
#         litchi_price = 0
#         product_name = ""
#         quantity = 0

#         option = int(input("Enter the option: "))

#         if option == 1:
#             quantity = int(input("Enter the quantity: "))
#             apple_price = 200 * quantity
#             product_name = "Apple"
#         elif option == 2:
#             quantity = int(input("Enter the quantity: "))
#             banana_price = 120 * quantity
#             product_name = "Banana"
#         elif option == 3:
#             quantity = int(input("Enter the quantity: "))
#             mango_price = 130 * quantity
#             product_name = "Mango"
#         elif option == 4:
#             quantity = int(input("Enter the quantity: "))
#             strawberries_price = 150 * quantity
#             product_name = "Strawberries"
#         elif option == 5:
#             quantity = int(input("Enter the quantity: "))
#             litchi_price = 140 * quantity
#             product_name = "Litchi"
#         else:
#             print("Invalid option")
#             continue

#         total = apple_price+banana_price+mango_price+strawberries_price+litchi_price
#         print("Your records have been saved!")

#         file.write(f"Customer name: {name}\n")
#         file.write(f"Product name: {product_name}\n")
#         file.write(f"Quantity: {quantity}\n")
#         file.write(f"Total: Rs.{total}\n")
#         file.write("\n")  

#         continue_option = input("Do you want to continue? (yes/no): ").lower()
#         if continue_option != 'yes':
#             print("Program stopped.")
#             break
#         else:
#             print("Program continued.")


