# Program to check if a number is prime or not

# To take input from the user
num = int(input("Enter a number: "))

# define a variable to track if the number is prime
is_prime = True

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

    # after the loop, check if is_prime is still True or False
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
