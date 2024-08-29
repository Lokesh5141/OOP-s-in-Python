"""
Two types of Variables : 
        1) " Instance Variables " : Created/Defined  inside the init 
           won't change for every Obj when they change any Obj

        2) "Class / Static Variables " : Created inside Class & Outside  __init__ 
            Can be change for every Obj even if a single change  and Accessable for every Obj

"""

class Car:


    wheels =4   # class / Static Variables 
    #will able to acess for every Obj and should bve change by using ClassName.ObjName = Updated value 


    def __init__(self) :
        self.mil=10             # milage  # these are instance Variables wont change for every obect
        self.comp='BMW'         # company



c1=Car()        # Obj of class
c2=Car()        # Obj of class

c1.mil=30             # changing Instance Variables
Car.wheels =12        # Changing Class Variables

print(f"Milage: {c1.mil} , Company :{c1.comp} , NO-of Wheels : {c1.wheels}")
print(f"Milage: {c2.mil} , Company :{c2.comp} , NO-of Wheels : {c2.wheels}")
