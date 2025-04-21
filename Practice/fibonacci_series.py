# Program to display the Fibonacci sequence up to n-th term

terms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


