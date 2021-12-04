
import re

from api.models.products import Products

#this variable will be used to validate email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# this variable will be used to validate password
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

allUser=[]
#this class works on the user
class User(Products):

    def __init__(self,userId,name,email,password,role):
        self.__name=name
        self.__email=email
        self.__password=password
        self.role=role
        self.__userId=userId
# the read only attributes for the name
    @property
    def name(self):
        return self.__name
# the read only attributes for the email
    @property
    def email(self):
        return self.__email
# the read only attributes for the password
    @property
    def password(self):
        return self.__password
      
    ##this method returns all users
    def users(self):
        return allUser
#this method add a single user in the allUsers list and returns the added user
    def addUser(self): 
       
        userInfo=[
            self.__userId==len(allUser)+1,
            self.category=='category',
            self.__name=='name',
            self.__email=='email',
            self.__password=='password',
            self.role=='role'
            ]
        if self.role is not 'Admin' or 'Attendant':
            return {'message':'roles can only be Admin and Attendant'}
        else:
            allUser.append(userInfo)
            return userInfo
  #this method returns details of a single sale      
    def singleUser(self):
        return allUser[self.__userId]

       
    def deleteUser(self):
        
        for user in allUser:
            user=[
            self.__userId=='id',
            self.category=='category',
            self.__name=='name',
            self.__email=='email',
            self.__password=='password',
            self.role=='role'
            ]
            allUser.remove(user)
            return user
       
    def validateEmail(self):
        
        if (re.fullmatch(regex, self.__email)):
            return {'message':'valid email!'}

        else:
            return {'message':'invalid email!'}
        
    
    def validatePassword(self):
        
        validity=True
        pattern=re.compile(reg)
        match=re.search(pattern,self.__password)
        if (len(self.__password)<8 or len(self.__password)>15):
            validity=False
        if match:
            validity=True

        else:
            validity=False


        return validity
        






