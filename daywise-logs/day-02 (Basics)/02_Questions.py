# Q4. Write a Python program to add two numbers entered by the user.

num1 = int(input("Enter First Number :- "))
num2 = int(input("Enter Second Number :- "))

total = num1 + num2

print(f"Total Value is {total}")


# Q5. Convert a string to an integer and vice versa.

day1 = 24
day2 = "25"
a = int(day2)
b = str(day1)
print(a, type(a))
print(b, type(b))


# Q6. Write a Python program to calculate the area of a rectangle using user
# input for length and width.

length = int(input("Length = "))
width = int(input("Width = "))

Area = length * width

print(f"Area of Rectangle = {Area}")


# Q7. Write a Python program to calculate the average of three numbers
# entered by the user.

num1 = int(input("Enter the 1st Number = "))
num2 = int(input("Enter the 2nd Number = "))
num3 = int(input("Enter the 3rd Number = "))

average = (num1 + num2 + num3) / 3

print(f"Average of three numbers is {average}")


# Q8. Convert a float to an integer and vice versa.

num1 = 34.65
print(num1, type(num1))

num_int = int(num1)
print(num_int, type(num_int))

# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.

F = float(input("Enter the Temprature in Fahrenheit : "))

C = (F - 32) * 5 / 9

print(f"Celsius = {C}")

# Q10. Calculate sum of 5 subjects and Find percentage.

sub1 = int(input("Enter the marks of Subject 1: "))
sub2 = int(input("Enter the marks of Subject 2: "))
sub3 = int(input("Enter the marks of Subject 3: "))
sub4 = int(input("Enter the marks of Subject 4: "))
sub5 = int(input("Enter the marks of Subject 5: "))

sum = sub1 + sub2 + sub3 + sub4 + sub5

percent = float((sum / 5))
print(f"Sum of 5 Subjects is {sum} and Percentage is {percent}")


# Q11. Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)

total_games = int(input("Enter the Total Number of Games Played = "))
win = int(input("Enter the total number of games you have win = "))
loss = int(input("Enter the total number of game you have lost = "))

tie = total_games - (win + loss)
points = (4 * win) + (2 * tie)

print(f"Total tie games is {tie} and total points is {points}")

# Q12 WAP in python to calculate user birth year. take input name and age.

name = input("Enter the Name: ")
age = int(input("Enter the age: "))

birth_year = 2025 - age

print(
    f"Hello {name},\nYour birth year is {birth_year} and current age is {age}. \nThanks !!"
)
