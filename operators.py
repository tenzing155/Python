#arithmetic operators
# addition
a = 5
b = 6
c = a + b
print(c)

#subtraction
a = 10
b = 5
print(a - b)

#multiplication
a= 100
b = 2
multiplication = a * b
print(multiplication)

#division
x = 10
y = 2
div = int(x / y)
print(div)

#modolus(remainder)
x = 11
y = 2
z = x % y
print(z)

#exponentiation(power)
x = 2
y = 4
exp = x ** y
print(exp)

#assignment operator
x = 5
x += 2    #x = x + 2
print(x)

x = 5
x -= 2    #x = x - 2
print(x)

x = 5 
x *= 2
print(x)

x = 4
x /= 2 
print(int(x))

x = 4
x %= 2
print(x)

#comparision operator

x = 5
y = 3
print(x == y)   #equal to

x = 10
y = 6
result = x != y     #not equal to
print(result)

x = 5
y = 10
print(x > y)        #greater than

x = 5
y = 10
print(x < y)        #less than

#logical operator
#and  #both condition should be true
x = 4
print(x > 2 and x <5)

#or #one condition needs to be true
x = 4
print(x > 2 or x <-1)

#not #result reverse 
x = 5
print(not(x>2 and x<6))

#operator precedence (left to right)
# 1.()
# 2.**
# 3.* /
# 4. + - 

#is, isnot, in
x = ['ram','sita']
y = ['ram', 'sita']
x = z
print(x is z)
print(x is y)
print(x is not z)

fruits = ['apple','banana']
vegetables = ['cauliflower', 'cabbage']
print('apple' in fruits) 
print(fruits is not vegetables)
