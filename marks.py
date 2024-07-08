print("Enter the marks of 5 subject :")
a = input()
b = input()
c = input()
d = input()
e = input()
total = a + b + c + d + e
percentage = int(total) / 5 * 100
if percentage >= 60 and percentage >= 100:
    print("Your grade is A")
elif percentage >= 45 and percentage >= 60:
    print("Your grade is B")
elif percentage >= 35 and percentage >=45:
    print("Your grade is C")
else:
    print("Fail")

