# DataTypes : Datatype specifies which type of value a Variable has.

"""
DOCSTRING !!!

Types of Datatype

1.Numeric Type :
        a) Interger: Integer is a +ve and -ve Whole Numbers like (2,55,1000,-99,-2892)
        b) Float : Float is a decimal number like (4.5,6.999,-200.001)
        c) Complex : Complex numbers are like {(2i+5j)+(3j-8k)}

2.Dictionary : Dictionary stores the multiple {"Key":Value}. In this Key cannot gets repeated but values can be same for differnt keys.

3.Sequence Type : Pending in Due Course
        a) List : List store multiple values of any datatypes in Single Variable. "eg. marks_of_10_student= [34,88,55,43,51,87,43,87,99,10] OR x=[abc,22.9,75,"Tushar",True]"
        b) Tuple : Tuple also store multiple values of any datatypes in Single Variable but it cannot change,update,delete or modify its value once its closed. "eg. info=("tushar",22,true)"
        c) String : Values that stores in "double quotes" or 'Single quotes' called Strings.

4.Sets : Pending in Due Course

5.Bool : Boolean is just a value that contain True or False
"""

x = 55
print(x)
print(type(x))
# Or
print(x, type(x))  # Integer.

y = 88.0
print(y, type(y))  # Float

z = True
print(z, type(z))  # Boolean

name = "Tushar Mandali"
print(name, type(name))  # String


marks = [33, 55, 22, 51]
print(marks, type(marks))  # List

marks = (33, 55, 22, 51)
print(marks, type(marks))  # Tuple

marks = {"Tushar": 89, "Yash": 78, "Shruti": 89}
print(marks, type(marks))  # Dictionary

##############################################################################################################################################

# Type Conversion and Type Casting : Convert Datatype to another datatype

x = "100.10"  # string Value
y = "200"

a = float(x)  # Converting to Integer
b = int(y)
z = a + b
print(z, type(z))

# String :

print(
    """My Name is Tushar 

Age is 21 
"""
)  # This is Multi-line String

# String Methods
print("Tushar".upper())
print("Tushar".lower())
print("TusHAR manDali".title())  # make starting letter all capital of the words
print("TusHAR manDali".islower())
print("tushar".islower())  # Check if the string contains all the lower char or not

# Complex Number :
num1 = 3 + 6
