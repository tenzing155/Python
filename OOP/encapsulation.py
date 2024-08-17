#Bundling of attributes and methods

class User:
    #password: public (anywhere and anyone)
    #_password: protected (Child)
    #__password: private (only its class and not others)
    __password = "ram002"

    @property
    def get_password(self):
        return self.__password
    
    @get_password.setter
    def get_password(self,password):
        self.__password = password

obj = User()
obj.get_password = "sita002"
print(obj.get_password)

