# print("hello python")
# print(34565)

# variable

# x=10
# y=50
# print(x+y)


# name='ram'
# address='ktm'


# print("my name is ",name,"address ",address)
# print(f"my name is {name} address {address}")

# name = input("Enter your name :")
# print(f"My name is {name}")

# # email
# email = input("Enter your email :")
# print(f"My email is {email}")

# #phone
# phone = input("Enter your phone number :")
# print(f"My phone number is {phone}")

# #age
# age = input("Enter your age :")
# print(f"My age is {age}")
# n1='ram'

# list -> []
# tuple -> ()
# set -> {}
# dictionary -> {}

# data=['ram','sita']
# print(data[0])

# name='ram'
# print(name.upper())
# print(dir(name))
# print(name[0])

# data=[]
# data.append("ram")
# data.append('sita')
# print(data)
# print(dir(data))


# data=['ram','sita']
# data.remove('ram')
# print(data)



# data=['ram','sita','ram','anil']
# data.append('gita')
# print(data)
# data.sort()
# print(data)
# print(data.count('ram'))
# data.pop()
# print(data)
# data.insert(0,'laxmi')
# print(data)
# data.clear()
# print(data)

# data=['ram','sita']
# data.index('ram')
# print(len(data))
# print(data)


# data=[
#     [23,[[[800]],500],67],
#     [67,[[900]],78]
# ]

# print(data[0][1][0][0])
# print(data[0][1][1])


# course ="we are learning python"
# print(course.upper())
# print(course.title())
# print(course.find("python"))
# print(course.index("learning"))
# print(course.isupper())
# print(course.islower())
# print(course.replace("we are","I am"))
#print(course.split())


#upper, title, find, index, isupper, islower, replace



# data=['ram','sita']

# key value pair

# data={
#     'name':'ram',
#     'age':45,
#     'address':'ktm',
#     'contact':{
#         'phone':9897,
#         'email':'ram@gmail.com'
#     }
# }

# print(data['name'])

# print(dir(data))

# print(data['contact']['email'])


# data=[
#     {'name':'ram'},
#     {'name':'sita'}
# ]

# print(data[1]['name'])


# data={
#     'name':'ram',
#     'contact':[
#         456767,
#         9456777
#     ]
# }

# print(data['contact'])


data={
    'name':'hari',
    'address':{
        'country':['nepal','china','india']
    },
    'contact':{
        'mobile':[9744654,988745],
        'email':['hari@gmail.com']
    }
}


# my name is hari i live in china contact me 9745455


# print(f"My name is {data['name']}")
# print(f"I live in {data['address']['country'][1]}")
# print(f"contact me {data['contact']['email'][0]}")


#methods
#clearing method
# data.clear()
# print(data)

#changing value
# data['address']['country'][0] = "bhutan"
# print(data)

#printing keys
# keys = data.keys()
# print(keys)

#printing values
# values = data.values()
# print(values)

#deleting key and values of dictiob
# data.pop('contact')
# print(data)

#updating values from key and also adding new key and value to dictionary
# data.update({'name': 'ram'})
# print(data)


