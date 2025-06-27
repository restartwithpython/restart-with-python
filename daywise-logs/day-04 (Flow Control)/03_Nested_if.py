# WAP in nested loop to check the entered number is Positive, Negative or Zero
num = int(input("Enter the Number : "))

if num >= 0:
    if num > 0:
        print(f"Entered Number {num} is Positive.")
    else:
        print(f"Entered Number {num} is Zero.")
else:
    print(f"Entered number {num} is Negative")

# Q38. Write a program that takes three numbers as input and determines the largest one using nested if-else statements. Make sure all 3 numbers
#     entered by user are different.
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
num3 = int(input("Enter the Third Number : "))

if num1 != num2 != num3:
    if num1 > num2 and num1 > num3:
        print(f"First number {num1} is greater.")
    else:
        if num2 > num3:
            print(f"Second number {num2} is greater.")
        else:
            print(f"Third number {num3} is greater.")
else:
    print(f"You have entered duplicate number. Please Try Again")

# Q39. Write a program that checks if a given year is a leap year. Leap years are divisible by 4, but not by 100 unless they are also divisible by 400.
"""
Leap year rule:

1. A year is considered a leap year if it is divisible by 4.
2. However, if that year is also divisible by 100, it is not a leap year.
3. There is an exception to this rule: if the year is divisible by 400, it is a leap year.
"""
year = int(input("Enter the Year = "))

if year % 4 == 0 and year % 100 != 0:
    print(f"Enter Year {year} is Leap Year")
else:
    if year % 400 == 0 and year % 100 == 0:
        print(f"Enter Year {year} is Leap Year")
    else:
        print(f"Enter Year {year} is not Leap Year")

# Q40. Create a program that calculates the price of a movie ticket based on the age of the customer. If the customer is under 12, the ticket costs $5; if
#      they are between 12 and 65, the ticket costs $10; otherwise, it's $7.
age = int(input("Enter the Age = "))
if age < 12:
    print(f"Price of the ticket is $5.")
else:
    if 12 < age < 65:
        print(f"Price of the ticket is $10")
    else:
        print(f"Price of the ticket is $7")

"""
Q41. Write a program that calculates a person's BMI based on their height (in meters) and weight (in kilograms). Use the following formula: 
BMI = weight / (height^2). Then, classify the BMI according to the following ranges:
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater
"""
h = float(input("Enter your Height(Meter) = "))
w = float(input("Enter your Weight(KG)= "))

BMI = w / (h**2)

if BMI > 18.5:
    if 18.5 <= BMI <= 24.9:
        print(f"Your BMI range is {BMI} && Weight is Normal.")
    else:
        if 25 <= BMI <= 29.9:
            print(f"Your BMI range is {BMI} && Weight is Overweight.")
        else:
            print(f"Your BMI range is {BMI} && Weight is Obesity.")
else:
    print(f"Your BMI range is {BMI} && Weight is Underweight.")
