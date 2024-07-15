# print("Welcome to Mobile Bazaar")
# print("Please enter your credentials below: ")
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" and password == "123":
#     print("Welcome user")
#     print("=============Mobile Bazar============")
#     phone = int(input("Enter 1 for iphone and 2 for android: "))
#     if phone == 1:
#         print("1.Iphone11(Rs.65000)\n2.Iphone12(Rs.75000)\n3.Iphone13(Rs.85000)\n4.Iphone14(Rs.95000)\n5.Iphone15(Rs.105000)")
        
#         iphone11_price = 0
#         iphone12_price = 0
#         iphone13_price = 0
#         iphone14_price = 0
#         iphone15_price = 0
#         product_name = 0
#         quantity = 0

#         option = int(input("Enter the option: "))

#         if option == 1:
#             quantity = int(input("Enter the quantity: "))
#             iphone11_price = 65000*quantity
#             product_name = "Iphone11"
#         elif option == 2:
#             quantity = int(input("Enter the quantity: "))
#             iphone12_price = 75000*quantity
#             product_name = "Iphone12"
#         elif option == 3:
#             quantity = int(input("Enter the quantity: "))
#             iphone13_price = 85000*quantity
#             product_name = "Iphone13"
#         elif option == 4:
#             quantity = int(input("Enter the quantity: "))
#             iphone14_price = 95000*quantity
#             product_name = "Iphone14"
#         elif option == 5:
#             quantity = int(input("Enter the quantity: "))
#             iphone15_price = 105000*quantity
#             product_name = "Iphone15"
#         else:
#             print("Invalid option")
#             exit()

#         total = iphone11_price+iphone12_price+iphone13_price+iphone14_price+iphone15_price
#         print("Delivery option: 1.Home Delivery(Rs.1000) 2.Pick up(free)")
#         delivery_option = int(input("Enter the delivery option:"))
#         delivery_price = 0
#         if delivery_option == 1:
#             delivery_price = 1000
#         else:
#             delivery_price = 0

#         print("Packing: 1. Plastice bag(Rs.1000) 2.Bag(Rs.2000) 3.Gift Box(Rs.3000)")
#         packing_option = int(input("Enter the packing option: "))
#         packing_price = 0
#         if packing_option == 1:
#             packing_price = 1000
#         elif packing_option == 2:
#             packing_price = 2000
#         elif packing_option == 3:
#             packing_price = 3000

#         print("Payment option: 1.Cash On Delivery 2.Online payment:")
#         payment_option = int(input("Enter the payment option:"))
#         if payment_option == 1:
#             payment = "Cash on Delivery"
#         else:
#             payment = "Online payment"


#         grand_total = total + delivery_price + packing_price 

#         print("================Bill================")
#         print("Product name:",product_name)
#         print("Quantity:",quantity)
#         print("Total:",total)
#         print("Delivery Price:",delivery_price)
#         print("Packing Price:",packing_price)
#         print("Grand Total :", grand_total)
#         print("Payment type :", payment)
#         print("Thank you Please visit us again!")


#     elif phone == 2:
#         print("1.Poco(Rs.50000)\n2.Redmi(Rs.40000)\n3.Xiaomi(Rs.60000)\n4.Vivo(Rs.35000)\n5.Oppo(Rs.32000)")

#         poco_price = 0
#         redmi_price = 0
#         xiaomi_price = 0
#         vivo_price = 0
#         oppo_price = 0
#         product_name = 0
#         quantity = 0

#         option = int(input("Enter the option: "))

#         if option == 1:
#             quantity = int(input("Enter the quantity: "))
#             poco_price = 50000*quantity
#             product_name = "Poco"
#         elif option == 2:
#             quantity = int(input("Enter the quantity: "))
#             redmi_price = 40000*quantity
#             product_name = "Redmi"
#         elif option == 3:
#             quantity = int(input("Enter the quantity: "))
#             xiaomi_price = 60000*quantity
#             product_name = "Xiaomi"
#         elif option == 4:
#             quantity = int(input("Enter the quantity: "))
#             vivo_price = 35000*quantity
#             product_name = "Vivo"
#         elif option == 5:
#             quantity = int(input("Enter the quantity: "))
#             oppo_price = 32000*quantity
#             product_name = "Oppo"
#         else:
#             print("Invalid option")
#             exit()

#         total = poco_price+redmi_price+xiaomi_price+vivo_price+oppo_price
#         print("Delivery option: 1.Home Delivery(Rs.1000) 2.Pick up(free)")
#         delivery_option = int(input("Enter the delivery option:"))
#         delivery_price = 0
#         if delivery_option == 1:
#             delivery_price = 1000
#         else:
#             delivery_price = 0

#         print("Packing: 1. Plastice bag(Rs.1000) 2.Bag(Rs.2000) 3.Gift Box(Rs.3000)")
#         packing_option = int(input("Enter the packing option: "))
#         packing_price = 0
#         if packing_option == 1:
#             packing_price = 1000
#         elif packing_option == 2:
#             packing_price = 2000
#         elif packing_option == 3:
#             packing_price = 3000

#         print("Payment option: 1.Cash On Delivery 2.Online payment:")
#         payment_option = int(input("Enter the payment option:"))
#         if payment_option == 1:
#             payment = "Cash on Delivery"
#         else:
#             payment = "Online payment"


#         grand_total = total + delivery_price + packing_price 

#         print("================Bill================")
#         print("Product name:",product_name)
#         print("Quantity:",quantity)
#         print("Total:",total)
#         print("Delivery Price:",delivery_price)
#         print("Packing Price:",packing_price)
#         print("Grand Total :", grand_total)
#         print("Payment type :", payment)
#         print("Thank you Please visit us again!")

#     else:
#         print("Please select the available options.")
# else:
#     print("Please enter correct username and password")


# print("=============ATM==============")
# print("Enter your pin.")
# pin = int(input())
# if pin == 1234:
#     print("Welcome user. Select the operation:")
#     print("1.Withdraw  2.Deposit  3.Check balance")
#     total = 100000
#     operation = int(input())
#     if operation == 1:
#         print("Put the amount you want to withdraw.")
#         withdraw_amount = int(input())
#         balance = total - withdraw_amount
#         print(f"You have successfully withdrawn Rs.{withdraw_amount}")
#         print(f"Your remaining balance is Rs.{balance}")
#         new_total = balance
#     elif operation == 2:
#         print("Put the amount you want to deposit.")
#         deposit = int(input())
#         balance = total + deposit
#         print(f"You have successfully deposited Rs.{deposit}")
#         print(f"Your remaining balance is Rs.{balance}")
#         new_total = balance
#     elif operation == 3:
#         print(f"Your balance is {total}")
#     else:
#         print("Wrong operation.")
# else:
#     print("Incorrect Pin.")


#WAP to create a bus ticketing system.
# Kathmandu - Pokhara - Rs1200
# Dharan - Chitwan - Rs 2600
# Ithari - Birgunj - Rs.2500
# Tourist - extra -120
# Single - same price
# couple - 2200, 2300, 2200

# print("============ BUS TICKETING SYSTEM =============")
# print("- Destination -")
# print("1. Kathmandu - Pokhara : Rs.1200")
# print("2. Dharan - Chitwan : Rs.2600")
# print("3. Itahari - Birgunj : Rs.2500")
# print("Note : If you are a foreigner extra 120 charges is applied.")

# destination = int(input("Enter your destination: "))
# foreigner = input("Are you a foreigner ? yes or no : ")
# print("Are you booking for a single or couple ride ?")
# print("1.Single \n2.Couple")
# partner = int(input())
# ticket = 0
# if destination == 1:
#     if foreigner == "yes":
#         if partner == 1:
#             ticket = 1200 + 120
#             print("Destination : Kathmandu to Pokara")
#             print("Enjoy your solo ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#         elif partner == 2:
#             ticket = 2200 + 120
#             print("Destination : Kathmandu to Pokara")
#             print("Enjoy your couple ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#     elif foreigner == "no":
#         if partner == 1:
#             ticket = 1200
#             print("Destination : Kathmandu to Pokara")
#             print("Enjoy your solo ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#         elif partner == 2:
#             ticket = 2200
#             print("Destination : Kathmandu to Pokara")
#             print("Enjoy your couple ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#     else:
#         print("Please enter correct parameter.")
# elif destination == 2:
#     if foreigner == "yes":
#         if partner == 1:
#             ticket = 2600 + 120
#             print("Destination : Dharan to Chitwan")
#             print("Enjoy your solo ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#         elif partner == 2:
#             ticket = 2300 + 120
#             print("Destination : Dharan to Chitwan")
#             print("Enjoy your couple ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#     elif foreigner == "no":
#         if partner == 1:
#             ticket += 2600
#             print("Destination : Dharan to Chitwan")
#             print("Enjoy your solo ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#         elif partner == 2:
#             ticket += 2300
#             print("Destination : Dharan to Chitwan")
#             print("Enjoy your couple ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#     else:
#         print("Please enter correct parameter.")
    
# elif destination == 3:
#     if foreigner == "yes":
#         if partner == 1:
#             ticket = 2500 + 120
#             print("Destination : Itahari to Birgunj")
#             print("Enjoy your solo ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#         elif partner == 2:
#             ticket = 2200 + 120
#             print("Destination : Ithari to Birgunj")
#             print("Enjoy your couple ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#     elif foreigner == "no":
#         if partner == 1:
#             ticket = 2500
#             print("Destination : Itahari to Birgunj")
#             print("Enjoy your solo ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#         elif partner == 2:
#             ticket = 2200
#             print("Destination : Ithari to Birgunj")
#             print("Enjoy your couple ride!")
#             print(f"Your ticket is Rs {ticket}. Thank you !")
#     else:
#         print("Please enter correct parameter.")
# else:
#     print("Please enter correct option.")


#Food order system
# 18 less - 10% dis
#stop - execute
#all total - stop

# print("===============FOOD ORDERING SYSTEM===============")
# print("Menu: ")
# print("1. Thakali food - Rs.450")
# print("2. Burger - Rs.240")
# print("3. Pizza - Rs.230")
# print("4. Momo - Rs.110")
# print("5. Chowmein - Rs.100")
# print("6. Thukpa - Rs.250")
# print("7. Sekuwa - Rs.80")
# print("8. Keema noodles - Rs.265")

# while True:
#     menu = input("Please choose your menu: ")
#     quantity = int(input("Enter the quantity: "))
#     print("Type 'stop' to execute and see the total.")
#     total_bill = 0
#     item_price = 0
#     food = 0    
#     if menu == 1:
#         item_price += 450
#         food += "Thakali food"
#     elif menu == 2:
#         item_price += 240
#         food += "Burger"
#     elif menu == 3:
#         item_price += 230
#         food += "Pizza"
#     elif menu == 4:
#         item_price += 110
#         food += "Momo"
#     elif menu == 5:
#         item_price = 100
#         food += "Chowmein"
#     elif menu == 6:
#         item_price += 250
#         food += "Thukpa"
#     elif menu == 7:
#         item_price += 80
#         food += "Sekuwa"
#     elif menu == 8:
#         item_price += 265
#         food += "Keema noodles"
#     elif menu.lower() == "stop":
#         break
#     else:
#         print("Enter correct menu parameter.")

#     total_item = item_price * quantity
#     total_bill += total_item

#     print("================Bill================")
#     print(f"Food: {food}")
#     print(f"Quantity: {quantity}")
#     print(f"Total for this item: Rs.{total_item}")

#     print(f"Your total bill is: Rs.{total_bill}")
#     print("Thank you! Please visit us again!")
