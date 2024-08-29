"""
if thir is no exception --> Try block won't Jumps into the except block 
So "You should'nt be exit the File or a DataBase in the 'Except block' "
Always ensure that to exit File in the final block coz it'll always execute even error Occurs or Not 

"""


a=15
b=5

try:
    print("Resource Open")
    print(a/b)
    Num=int(input("Enter Your Number :"))
    print(Num)


except ValueError as e:
    print("Invalid Input : ", e)

except ZeroDivisionError as e:    
    print("You cant able to perform divicible  by Zero : ",e)
    
except Exception as e:
    print("Unexpected Exception : Something went wring..!")
    

finally:
    print("Resource Closed")
    print('The End')



