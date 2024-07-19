print("Enter the marks of 5 subject :")
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



