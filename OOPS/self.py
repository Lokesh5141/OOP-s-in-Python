class computer:
    def __init__(self) :
        self.name='loki'
        self.age=21
    def update(self):
        self.age=22
        self.name='Lavada'


c1=computer()
c2=computer()

c1.name='Lokesh'
c1.age=56

c1.update()
print(c1.name)
print(c1.age)

print(c2.name)
print(c2.age)



"""
print(c1)
print(c2)
"""

print(id(c1))
print(id(c2))