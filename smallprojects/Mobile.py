print("=============Mobile Bazar============")
phone = int(input("Enter 1 for iphone and 2 for android: "))
if phone == 1:
    print("1.Iphone11(Rs.65000)\n2.Iphone12(Rs.75000)\n3.Iphone13(Rs.85000)\n4.Iphone14(Rs.95000)\n5.Iphone15(Rs.105000)")
    
    iphone11_price = 0
    iphone12_price = 0
    iphone13_price = 0
    iphone14_price = 0
    iphone15_price = 0
    product_name = 0
    quantity = 0

    option = int(input("Enter the option: "))

    if option == 1:
        quantity = int(input("Enter the quantity: "))
        iphone11_price = 65000*quantity
        product_name = "Iphone11"
    elif option == 2:
        quantity = int(input("Enter the quantity: "))
        iphone12_price = 75000*quantity
        product_name = "Iphone12"
    elif option == 3:
        quantity = int(input("Enter the quantity: "))
        iphone13_price = 85000*quantity
        product_name = "Iphone13"
    elif option == 4:
        quantity = int(input("Enter the quantity: "))
        iphone14_price = 95000*quantity
        product_name = "Iphone14"
    elif option == 5:
        quantity = int(input("Enter the quantity: "))
        iphone15_price = 105000*quantity
        product_name = "Iphone15"
    else:
        print("Invalid option")
        exit()

    total = iphone11_price+iphone12_price+iphone13_price+iphone14_price+iphone15_price
    print("Delivery option: 1.Home Delivery(Rs.1000) 2.Pick up(free)")
    delivery_option = int(input("Enter the delivery option:"))
    delivery_price = 0
    if delivery_option == 1:
        delivery_price = 1000
    else:
        delivery_price = 0

    print("Packing: 1. Plastice bag(Rs.1000) 2.Bag(Rs.2000) 3.Gift Box(Rs.3000)")
    packing_option = int(input("Enter the packing option: "))
    packing_price = 0
    if packing_option == 1:
        packing_price = 1000
    elif packing_option == 2:
        packing_price = 2000
    elif packing_option == 3:
        packing_price = 3000

    print("Payment option: 1.Cash On Delivery 2.Online payment:")
    payment_option = int(input("Enter the payment option:"))
    if payment_option == 1:
        payment = "Cash on Delivery"
    else:
        payment = "Online payment"


    grand_total = total + delivery_price + packing_price 

    print("================Bill================")
    print("Product name:",product_name)
    print("Quantity:",quantity)
    print("Total:",total)
    print("Delivery Price:",delivery_price)
    print("Packing Price:",packing_price)
    print("Grand Total :", grand_total)
    print("Payment type :", payment)
    print("Thank you Please visit us again!")


elif phone == 2:
    print("1.Poco(Rs.50000)\n2.Redmi(Rs.40000)\n3.Xiaomi(Rs.60000)\n4.Vivo(Rs.35000)\n5.Oppo(Rs.32000)")

    poco_price = 0
    redmi_price = 0
    xiaomi_price = 0
    vivo_price = 0
    oppo_price = 0
    product_name = 0
    quantity = 0

    option = int(input("Enter the option: "))

    if option == 1:
        quantity = int(input("Enter the quantity: "))
        poco_price = 50000*quantity
        product_name = "Poco"
    elif option == 2:
        quantity = int(input("Enter the quantity: "))
        redmi_price = 40000*quantity
        product_name = "Redmi"
    elif option == 3:
        quantity = int(input("Enter the quantity: "))
        xiaomi_price = 60000*quantity
        product_name = "Xiaomi"
    elif option == 4:
        quantity = int(input("Enter the quantity: "))
        vivo_price = 35000*quantity
        product_name = "Vivo"
    elif option == 5:
        quantity = int(input("Enter the quantity: "))
        oppo_price = 32000*quantity
        product_name = "Oppo"
    else:
        print("Invalid option")
        exit()

    total = poco_price+redmi_price+xiaomi_price+vivo_price+oppo_price
    print("Delivery option: 1.Home Delivery(Rs.1000) 2.Pick up(free)")
    delivery_option = int(input("Enter the delivery option:"))
    delivery_price = 0
    if delivery_option == 1:
        delivery_price = 1000
    else:
        delivery_price = 0

    print("Packing: 1. Plastice bag(Rs.1000) 2.Bag(Rs.2000) 3.Gift Box(Rs.3000)")
    packing_option = int(input("Enter the packing option: "))
    packing_price = 0
    if packing_option == 1:
        packing_price = 1000
    elif packing_option == 2:
        packing_price = 2000
    elif packing_option == 3:
        packing_price = 3000

    print("Payment option: 1.Cash On Delivery 2.Online payment:")
    payment_option = int(input("Enter the payment option:"))
    if payment_option == 1:
        payment = "Cash on Delivery"
    else:
        payment = "Online payment"


    grand_total = total + delivery_price + packing_price 

    print("================Bill================")
    print("Product name:",product_name)
    print("Quantity:",quantity)
    print("Total:",total)
    print("Delivery Price:",delivery_price)
    print("Packing Price:",packing_price)
    print("Grand Total :", grand_total)
    print("Payment type :", payment)
    print("Thank you Please visit us again!")

else:
    print("Please select the available options.")