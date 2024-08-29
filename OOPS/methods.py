"""
Methods 3 types :
 
" INSTANCE METHODS " : called by "self" keyword inside it 
           -- instance variable can be used with instance Methods 
           --  ex: " Accessers " : Geetters and 
                   " Mutators "  : Setters

" Class Methods "    : cadded by "cls" keyword inside it and 
            -- Class variable can be used with Class Methods 
            -- we need to add "Decorator" to it  @ Classmethod

" Static Methods "   : not consernd abt instance and class methods and wanna do some other operation

"""
from typing import Any


class Student:

    University="Kakatiya Unniversity"  #  Class Vairable

    def __init__(self,m1,m2,m3):    # constructor will call for every Obj in the class
        self.m1=m1   # Instance Variables
        self.m2=m2
        self.m3=m3

    def avg(self):    #instance method
        return (self.m1+self.m2+self.m3)/3  #it'll just return You need to Print 
        
    def get_m1(self):    #Getter instance Method
        return self.m1           #it'll just return You need to Print 
        
    
    def set_m1(self,value):    # Setter Instance Method
         self.m1=value            # not need to methon return Statement here
        
    @classmethod
    def get_Uni(cls):        # returning the class variable with class method
        return cls.University
    
    def info():
        print(" This is Static Method which Helps to to any Operatioin without Conserning of Class and Instance Methods")

s1=Student(12,45,76)   # every  Object are allways Call through Constructor 
s2=Student(95,68,46)


print(f"Getting the marks_1 for Student1 : {s1.get_m1()}")  # printing the  Getter instance Method

s1.set_m1(55) # it'll set the  value perminantly 

print(s1.m1)

print(f"Average  Marks of Student1 : {s1.avg()}")  # printing the Avg

print(s1.get_Uni())

print(f"University : {Student.get_Uni()}")

print(Student.info())
#  print(s1.m1) # insted of call directly we can call / Get through  Getter method




