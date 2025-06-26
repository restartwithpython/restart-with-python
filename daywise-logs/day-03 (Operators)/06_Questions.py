# Q: What is the difference between is and ==?
# "==" Operator Checks whether the values of two variables are equal.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True → values are same

# but in "is" it Checks whether two variables point to the same memory location (same object / Identity (same memory)	).

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False → different objects, even if values are same

"""
What will be the output of:
result = 3 + 2 * 5 ** 2 // 2 - 1
print(result)

5 ** 2 = 25

2 * 25 = 50

50 // 2 = 25

3 + 25 = 28

28 - 1 = 27

Answer is : 27
"""
# Output goes from left to right using BODMAS Rule
# 1. Exponentiation
# 2. Multiplication, division, floor division, Modulo (Left to Right)
# 3. Addition and Substraction (Left to Right)

"""
Q: Write a Python script:

Takes user name, age, and gender
Calculates birth year
If age > 18 and gender == "male", print "You are an adult male born in <year>"
Else print "You are either underage or not male"

"""

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
gender = input("Enter your Gender: ")

birth_year = 2025 - age

print(
    f"Hello {name},\nYour Age is {age}.Your Gender is {gender} and your Birth Year is {birth_year}."
)

if age > 18 and (gender == "Male" or gender == "male"):
    print(f"You are an adult Male born in year {birth_year}.")
else:
    print(f"You are either underage or not Male.")
