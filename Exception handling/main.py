#exception : Events occured during execution that interrupts flow of program (error)
try:
    numerator = int(input("Enter a numerator:"))
    denominator = int(input("Enter a denominator:"))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("It always gets execute")