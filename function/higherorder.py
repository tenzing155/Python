#higher order function takes one or more function as argument or returns a function.

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello")
#     print(text)

# hello(loud)

#map function - function, using that function to iterable objects

# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)

# def cube(a):
#     return a ** 3

# numbers = [1,2,3,4,5]
# cubed_numbers = list(map(cube,numbers))
# print(cubed_numbers)

# def add(x,y):
#     return x + y

# number_a = 1,3,5
# number_b = 2,4,6
# answer = list(map(add,number_a,number_b))
# print(answer)

#filter function : filters out the iterable item through a function 
# def even(x):
#     return x % 2 == 0 

# numbers = [1,2,3,4,5,6,7,8,9,10]

# even_num = list(filter(even,numbers))
# print(even_num)

# def odd(x):
#     return x % 3 == 0

# numbers = [2,3,4,6,8,9,7]
# odd_num = list(filter(odd,numbers))
# print(odd_num)