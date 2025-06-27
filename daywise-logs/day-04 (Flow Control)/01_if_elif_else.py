# IF Statement :
"""
Syntax
if condition: {Condition Value output must be True/False}
    code  {Here the 4 space between starting to code and it is known as Indentation }
    code
    code
else:
    code
    code
    code
"""
age = int(input("Enter age = "))
if age >= 18:
    print("You can Vote")
else:
    print("You cannot Vote")
print("Done")

# WAP to print the greatest number
num1 = int(input("Enter 1 no. = "))
num2 = int(input("Enter 2 no. = "))

if num1 > num2:
    print(f"{num1} is the greatest number.")

else:
    print(f"{num2} is the greatest number.")

# WAP to print the number is odd or even

num1 = int(input("Enter the Number = "))

if num1 % 2 == 0:
    print(f"{num1} is an Even Number")

else:
    print(f"{num1} is an Odd Number")


# WAP to get result pass or fail

physics = int(input("Enter the Physics Marks = "))
chemistry = int(input("Enter the Chemistry Marks = "))

if physics > 35 and chemistry > 35:
    print("Pass !!")
else:
    print("Fail...")

# -------------------------------------------------------------------------------------------------------------------------------------------------
# If elif Statement
"""
Syntax 
if Condition:           if condition 1 is true then it will not check any other condition 
    Code
    Code
    Code
elif Condition:
    Code
    Code
    Code
else :          else is not compulsary 
    Code 
    Code 
    Code


"""


# Ask 2 number from user and print which is greatest

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

if num1 > num2:
    print("Num 1 is greater.")
elif num2 > num1:
    print("Num 2 is greater.")
else:
    print("Both numbers are equal.")


# Question 2

subj1 = int(input("Enter the marks of Subject 1 : "))
subj2 = int(input("Enter the marks of Subject 2 : "))
subj3 = int(input("Enter the marks of Subject 3 : "))
subj4 = int(input("Enter the marks of Subject 4 : "))
subj5 = int(input("Enter the marks of Subject 5 : "))

percent = (subj1 + subj2 + subj3 + subj4 + subj5) / 5

if 100 > percent > 90:
    print("A Grade")
elif 90 > percent > 80:
    print("B Grade")
elif 80 > percent > 70:
    print("C Grade")
elif 70 > percent > 60:
    print("D Grade")
elif 0 < percent < 61:
    print("Fail")
else:
    print("INVALID")
