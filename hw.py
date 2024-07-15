#Takes 10 student name and prints grade.
i = 0
while (i <= 10):
    name = input("Enter the name of student:")
    print(f"Enter the marks of {name} for 5 subject :")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    total = a + b + c + d + e
    print(f"Total marks = {total}")
    percentage = (total / 500) * 100
    print(f"Your percentage = {percentage}")
    if percentage > 75 and percentage <= 100:
        print("Your grade is A")
    elif percentage > 60 and percentage <= 75:
        print("Your grade is B")
    elif percentage > 45 and percentage <= 60:
        print("Your grade is C")
    elif percentage > 35 and percentage <= 45:
        print("Your grade is D")
    else:
        print("Fail")
    i += 1
    option = input("Enter 'stop' to stop the result or 'continue':")
    if option == 'stop':
        print("Result stopped")
        break
    elif option == 'continue':
        print("Result continued")
        continue
    else:
        print("Enter correct paramter.")
        exit()
    
#Multiple of user inputted number: 
num = int(input("Enter a number:"))
i = 1
while (i <= 10):
    print(num * i)
    i += 1