# categories = [
#     {'id': 1, 'name':'laptop'},
#     {'id': 2, 'name':'mobile'},
#     {'id': 3, 'name':'tablet'}
# ]

# products = [
#     {'id':1,'name':'dell','category_id':1},
#     {'id':2,'name':'mac','category_id':1},
#     {'id':3,'name':'iphone','category_id':2},
#     {'id':4,'name':'samsung','category_id':2},
#     {'id':5,'name':'ipad','category_id':3},
#     {'id':6,'name':'samsung tab','category_id':3},
# ]

# laptop
# dell
# mac
# mobile
# iphone
# samsung

# for category in categories:
#     print(category['name'])
#     for product in products:
#         if category['id'] == product['category_id']:
#             print(" \t",product['name'])


# category_input = input("Enter category: (laptop,mobile,tablet): ")
# for category in categories:
#     if category_input == category['name'] == 'laptop':
#         print(category['name'])
#         for product in products:
#             if category['id'] == product['category_id']:
#                 print(" \t",product['name'])
#     elif category_input == category['name'] == 'mobile':
#         print(category['name'])
#         for product in products:
#             if category['id'] == product['category_id']:
#                 print(" \t",product['name'])
#     elif category_input == category['name'] == 'tablet':
#         print(category['name'])
#         for product in products:
#             if category['id'] == product['category_id']:
#                 print(" \t",product['name'])
    


# name = input("Enter the category name:")
# for category in categories:
#     if category['name'] == name:
#         print(category['name'])
#         for product in products:
#             if category['id'] == product['category_id']:
#                 print(" \t",product['name'])

    

# categories = [
#     {'id': 1, 'name':'laptop'},
#     {'id': 2, 'name':'mobile'},
#     {'id': 3, 'name':'tablet'}
# ]

# products = [
#     {'id':1,'name':'dell','category_id':1},
#     {'id':2,'name':'mac','category_id':1},
#     {'id':3,'name':'iphone','category_id':2},
#     {'id':4,'name':'samsung','category_id':2},
#     {'id':5,'name':'ipad','category_id':3},
#     {'id':6,'name':'samsung tab','category_id':3},
#     {'id':7,'name':'hp','category_id':1},
#     {'id':1,'name':'dell','category_id':1},
#     {'id':7,'name':'hp','category_id':1}
# ]

# remove duplicates
# repeat=[]
# name = input("Enter the product category: ")
# for category in categories:
#     if category['name']== name:
#         print(category['name'])
#         for product in products:
#             if category['id']==product['category_id']:
#                 if product['name'] not in repeat:
#                     repeat.append(product['name'])
#                     print('\t',product['name'])


# ascending order
# ascending = []
# name = input("Enter the product category: ")

# for category in categories:
#     if category['name'] == name:
#         print(category['name'])
#         for product in products:
#             if category['id'] == product['category_id']:
#                 if product['name'] not in ascending:
#                     ascending.append(product['name'])
        
#         ascending.sort()
#         for product_name in ascending:
#             print('\t', product_name)







# ecommerce
# productData = [
#     {'id':1,'name':'laptop', 'quantity':10,'price':50000},
#     {'id':2,'name':'mobile', 'quantity':20,'price':20000},
#     {'id':3,'name':'tablet', 'quantity':30,'price':10000},
#     {'id':4,'name':'desktop', 'quantity':40,'price':40000},
# ]

# productId, product name, quantity, total price
# 1          laptop           10       50000

# Displaying Products
# for product in productData:
#     print("Product id:",product['id'],"\t","Product name:",product['name'],"\t","Product quantity:",product['quantity'],"\t","Product price:",product['price'])
# Taking input from user for Product name and Quantity
# product_name = input("Enter Product name: ")
# product_quantity = int(input("Enter Product quantity: "))
# laptop = 0
# mobile = 0
# tablet = 0
# desktop = 0
# quantity = 0
# total_price = 0
# for product in productData:
#     if product['name'] == product_name:
#         if product_quantity <= product['quantity']:
#             print("Product name :",product['name'])
#             total_price = product_quantity * product['price'] 
#             print("---------------Bill---------------")
#             print("Product name :",product_name)
#             print("Product quantity",product_quantity)
#             print("Total =", total_price)
#         else:
#             print("Enter valid quantity.")
#             break


# *
# **
# ***
# ****
# *
# **
# ***
# ****

# for i in range(1,5):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
# for i in range(1,5):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
    
# 1
# 11
# 111
# 1111

# for i in range(5):
#     for j in range(1,i+1):
#         print("1", end="")
#     print()

# 1
# 12
# 123
# 1234
# for i in range(5):
#     for j in range(1,i+1):
#         print(j,end= "")
#     print()

# *
# **
# ***
# ****
# *moon*
# *********
# **********
# *
# **
# ***
# ****
# **sun**
# *********
# **********

# for row in range(1,7):
#     for column in range(1,row+1):
#         if row == 4:
#             if column == 4:
#                 print("*moon*",end ="")
#         else:
#             print("*",end="")
#     print()
# for row in range(1,7):
#     for column in range(1,row+1):
#         if row == 4:
#             if column == 4:
#                 print("*sun*",end ="")
#         else:
#             print("*",end="")
#     print()


# *****
# *****
# *****
# *****
# *****

# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()

# * 
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# *****
# ****
# ***
# **
# *

# for i in range(5):
#     for j in range(i,5):
#         print("*" , end="")
#     print()