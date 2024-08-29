"""
In Python, a constructor is created using the __init__ method. 
The __init__ method is a special method that is automatically called when an object is created from a class. 
 It allows you to initialize the object's attributes  
"""

class computer:
    def __init__(self,Name,Sex,Age):
        self.Name=Name
        self.Sex=Sex
        self.Age=Age



    def config(self):
        print(f"Hello {self.Name}")


   
     
com1=computer("Loki","Male",21)     #Object
com2=computer("Raki","Male",25)


#computer.config(com1)

com1.config()
com2.config()

"""
Don't do like this 
print(com1.Name())
print(com2.Name())

"""


print(com1.Name)
print(com2.Name)











