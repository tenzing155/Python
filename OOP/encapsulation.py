# Bundling of attributes and methods

# class User:
#     #password: public (anywhere and anyone)
#     #_password: protected (Child)
#     #__password: private (only its class and not others)
#     __password = "ram002"

#     @property
#     def get_password(self):
#         return self.__password
    
#     @get_password.setter
#     def get_password(self,password):
#         self.__password = password

# user = User()
# user.get_password = "sita002"
# print(user.get_password)



# class Admin:
#     __password = "admin123"

#     @property
#     def get_password(self):
#         return self.__password
    
#     @get_password.setter
#     def set_password(self,new_pass):
#         self.__password = new_pass


# user = Admin()
# user.set_password = "admin12345"
# print(user.get_password)


# class Person:
#     __name = "Hari"
#     __age = 18

#     @property
#     def get_info(self):
#         return self.name, self.__age
#     @get_info.setter
#     def set_info(self,info):
#         newname, newage = info
#         self.name = newname
#         self.age = newage

# p1 = Person()
# p1.set_info = ("Ram",20)
# print(p1.get_info)


# class Vechile:
#     __number = 123123

#     @property 
#     def get_number(self):
#         return self.__number
#     @get_number.setter
#     def set_number(self,value):
#         self.__number = value

# v1 = Vechile()
# v1.set_number = 321213
# print(v1.get_number)

class User:
    def __init__(self):
        self.__username = "user001"
        self.__password = "user123"

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value


user = User()


user.username = "user100"
user.password = "user10000"


print(user.username)  
print(user.password)   
