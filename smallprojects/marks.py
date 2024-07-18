# print("Enter the marks of 5 subject :")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# total = a + b + c + d + e
# print(f"Total marks = {total}")
# percentage = (total / 500) * 100
# print(f"Your percentage = {percentage}")
# if percentage > 75 and percentage <= 100:
#     print("Your grade is A")
# elif percentage > 60 and percentage <= 75:
#     print("Your grade is B")
# elif percentage > 45 and percentage <= 60:
#     print("Your grade is C")
# elif percentage > 35 and percentage <= 45:
#     print("Your grade is D")
# else:
#     print("Fail")


#100min
#1-10
#ntc to ntc -> 2.5
#ntc to ncell -> 3.5
#ncell to ncell ->5
#ncell to ntc -> 4

print("=============Call system============")
print("Enter sim to sim: \n")
print("Enter option\n1. ntc to ntc\n2. ntc to ncell\n3. ncell to ncell\n4. ncell to ntc\n ")
option = int(input())
time = int(input("Enter the time: "))
if time > 0  and time <= 100:
    if option == 1:
        bonus = 2.5
        if time > 1 and time < 10:
            new_bonus = bonus*1
        elif time > 11 and time < 20:
            new_bonus = bonus*2
        elif time > 21 and time < 30:
            new_bonus = bonus*3
        elif time > 31 and time < 40:
            new_bonus = bonus*4
        elif time > 41 and time < 50:
            new_bonus = bonus*5
        elif time > 51 and time < 60:
            new_bonus = bonus*6
        elif time > 61 and time < 70:
            new_bonus = bonus*7
        elif time > 71 and time < 80:
            new_bonus = bonus*8
        elif time > 81 and time < 90:
            new_bonus = bonus*9
        elif time > 91 and time < 100:
            new_bonus = bonus*10

        print("Bonus is", new_bonus)
    if option == 2:
        bonus = 3.5
        if time > 1 and time < 10:
            new_bonus = bonus*1
        elif time > 11 and time < 20:
            new_bonus = bonus*2
        elif time > 21 and time < 30:
            new_bonus = bonus*3
        elif time > 31 and time < 40:
            new_bonus = bonus*4
        elif time > 41 and time < 50:
            new_bonus = bonus*5
        elif time > 51 and time < 60:
            new_bonus = bonus*6
        elif time > 61 and time < 70:
            new_bonus = bonus*7
        elif time > 71 and time < 80:
            new_bonus = bonus*8
        elif time > 81 and time < 90:
            new_bonus = bonus*9
        elif time > 91 and time < 100:
            new_bonus = bonus*10
        print("Bonus is",new_bonus)
    if option == 3:
        bonus = 5
        if time > 1 and time < 10:
            new_bonus = bonus*1
        elif time > 11 and time < 20:
            new_bonus = bonus*2
        elif time > 21 and time < 30:
            new_bonus = bonus*3
        elif time > 31 and time < 40:
            new_bonus = bonus*4
        elif time > 41 and time < 50:
            new_bonus = bonus*5
        elif time > 51 and time < 60:
            bnew_bonus = bonus*6
        elif time > 61 and time < 70:
            new_bonus = bonus*7
        elif time > 71 and time < 80:
            new_bonus = bonus*8
        elif time > 81 and time < 90:
            new_bonus = bonus*9
        elif time > 91 and time < 100:
            new_bonus = bonus*10
        print("Bonus is", new_bonus)
    if option == 4:
        bonus = 4
        if time > 1 and time < 10:
            new_bonus = bonus*1
        elif time > 11 and time < 20:
            new_bonus = bonus*2
        elif time > 21 and time < 30:
            new_bonus = bonus*3
        elif time > 31 and time < 40:
            new_bonus = bonus*4
        elif time > 41 and time < 50:
            new_bonus = bonus*5
        elif time > 51 and time < 60:
            new_bonus = bonus*6
        elif time > 61 and time < 70:
            new_bonus = bonus*7
        elif time > 71 and time < 80:
            new_bonus = bonus*8
        elif time > 81 and time < 90:
            new_bonus = bonus*9
        elif time > 91 and time < 100:
            new_bonus = bonus*10
        print("Bonus is", new_bonus)
        
else:
    print("Time is invalid")
    




