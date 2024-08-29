class computer:
    def __init__(self,name="Loki",age=21):  # constructor --> intialize the objects and setting the default values in parremeters itself
        self.name=name
        self.age=age

    def update(self):  # update method
        self.name='raki'
        self.age=24

    def compare(self,other): # compare method 
        if self.name==other.name:
            return True
        else:
            return False


# if you want to pass the object without arguments   --> You need to set the default values in __init__ constructor parameters itself
c1=computer() # Objects of Computer Class
c2=computer()
c3=computer("Baki",468)

print(c1.name)   # call the object through constructor
print(c2.name)   # print in the sequence 
print(c2.age)

c3.update()   # Update the c2 object through update method with self and print it
print(c3.name)
print(c3.age)

if c1.compare(c2):  # print the 
    print("they Are Same")
else:
    print("They are Not Same")



