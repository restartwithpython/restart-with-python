# Q12. Write a Python program that takes two numbers as input and performs the following operations:
# addition, subtraction, multiplication,division, and modulus. Display the results.

num1 = int(input("Enter the 1st Number = "))
num2 = int(input("Enter the 2nd Number = "))

print(f"Addition of {num1} and {num2} is {num1 + num2}")
print(f"Substraction of {num1} and {num2} is {num1 - num2}")
print(f"Multipication of {num1} and {num2} is {num1 * num2}")
print(f"Division of {num1} and {num2} is {num1 / num2}")
print(f"Reminder of {num1} and {num2} is {num1 % num2}")


# Q13. Write a Python program to swap the values of two variables without using a temporary variable.

num1 = int(input("Enter the 1st Number = "))
num2 = int(input("Enter the 2nd Number = "))

num1 = num1 + num2  # a = a + b
num2 = num1 - num2  # b = a - b
num1 = num1 - num2  # a = a - b

print(f"The swap number are {num1} and {num2}")


# Q14. Write a Python program to calculate the compound interest for a
# given principal, rate of interest, and time period. Ask everything from the user.

p = float(input("Enter the Principal Value = "))
r = float(input("Enter the Rate of Intrest = "))
n = float(input("Enter the Number of times intrest is compounded per year = "))
t = float(input("Enter the Time period in Year ="))
CI = p * (1 + r / n) ** t

print(f"Compound Intrest = {CI} ")

# Q15. Write a Python program that takes the radius of a circle as input and
# calculates its area. Use the formula: Area = 3.14 * r^2.

radius = float(input("Enter the raidus of circle : "))

Area = 3.14 * (radius**2)

print(f"Area of circle is {Area}")
