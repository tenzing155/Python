num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter the operator: (+,-,*,/,%) ")
match(operator):
    case '+':
        sum = num1 + num2
        print("The sum is ", sum)
    case '-':
        sub = num1 - num2
        print("The subtraction is ",sub)
    case '*':
        mul = num1 * num2
        print("The multiplication is", mul)
    case '/':
        div = num1 / num2
        print("The div is ", div)
    case '%':
        mod = num1 % num2
        print("The modulus is",mod)
    case _:
        print("Invalid operator.")