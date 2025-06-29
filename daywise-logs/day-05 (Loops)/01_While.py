"""
While : If the given condition is true it will execute the condition continuously until it gets false.
If the condition is true it will execute all the code inside the while

Syntax

While Condition :
    Code
    Code
    Code
"""

# WAP to print Hello World 10 times in a row.
i = 1
while i <= 10:
    print("Hello Tushar")
    i += 1
    print("Done")
    print("OK Bye")

# WAP to print 1 to 10 number using While
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

# WAP to print Even Number from 1 to 20.
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1


# Q42. Ask a number from user. Print all the numbers from 1 to that number.
# num = int(input("Enter The Number = "))
i = 1
while i <= num:
    print(i, end=(" "))
    i += 1

# Q43. Ask a number (N) from user. Print all the numbers from N to 1.
num = int(input("Enter the Number = "))
while num >= 1:
    print(num, end=(" "))
    num -= 1

# Q44. Ask start number and end number from user. Print all the numbers from start to end using while loop.
num1 = int(input("Enter the Starting Number = "))
num2 = int(input("Enter the Ending Number = "))

while num1 <= num2:
    print(num1, end=" ")
    num1 += 1

# Q45. Calculate the sum of all the numbers from 1 to 10.
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i += 1
print(sum)

# Q46. Calculate product of all the numbers from 1 to 10.
i = 1
product = 1
while i <= 10:
    product = product * i
    i += 1
print(product)

# Q47. Calculate how many numbers are divisible by 7 from 1 to 100.
i = 1
num = 0
while i <= 100:
    if i % 7 == 0:
        print(i, end=" ")
        num += 1

    i += 1
print(f"\nThere are {num} numbers are divisible by 7 in 1 to 100")

# Q48. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
i = 1
num = 0
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        print(i, end=" ")
        num += 1
    i += 1
print(f"\nThere are {num} numbers are divisible by both 6 and 7 in 1 to 200")

# Q49. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.
i = 20
sum = 0
while i <= 50:
    if i % 4 == 0:
        print(i, end=" ")
        sum = sum + i
    i += 1
print(f"\nThe sum of all the numbers divisible by 4 from 20 to 50 is {sum}")

# Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.
i = 1
num = 0
while i <= 200:
    if i % 6 == 0 or i % 7 == 0:
        print(i, end=" ")
        num += 1
    i += 1
print(f"\nThere are {num} numbers which is divisible by 6 and 7 between 1 to 200")

"""
Q51. Ask a number from user. Print the multiplication table of that number.
Example
Enter a number = 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 10 = 80
"""
num = int(input("Enter the Number = "))
i = 1
while i <= 10:
    prod = num * i
    print(num, " X ", i, " = ", prod)
    i += 1

"""
Q52. Calculate factorial of a number entered by user.
Example:
Enter a number = 5
Factorial of a number means product of all the numbers from 1 to that
number.
5 factorial = 5 x 4 x 3 x 2 x 1
Output = 120
"""
num = i = int(input("Enter the Number = "))
fact = 1
while i >= 1:
    fact = fact * i
    i -= 1
print(f"{num} Factorial is {fact}")

# Q53. Ask to numbers x and y from the user. If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x.
num1 = int(input("Enter the value of X = "))
num2 = int(input("Enter the value of Y = "))
if num1 <= num2:
    while num1 <= num2:
        print(num1, end=" ")
        num1 += 1
else:
    while num2 <= num1:
        print(num2, end=" ")
        num2 += 1
print(num1)
# While completed
