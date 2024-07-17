users=[
    {'username':'ram','password':'ram002'},
    {'username':'sita','password':'sita002'},
    {'username':'hari','password':'hari002'}, 
]

books =[
    {'name':'book1','author':'author1','price':100},
    {'name':'book2','author':'author2','price':200},
    {'name':'book3','author':'author3','price':300},
]


username = input("Enter your username: ")
password = input("Enter your password: ")

for user in users:
    if user['username'] == username and user['password'] == password:
        print("Here are the books! :")
        for book in books:
            print(f"Name : {book['name']}, Author : {book['author']}, Price : {book['price']}")

        break
else:
    print("Wrong credentials.") 