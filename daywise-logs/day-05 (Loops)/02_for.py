"""
For Loop :
Syntax :
for i in range (1,11):      #Here i range starts from 1 to 10. It will include the left number but exclude the right number.
    Code()                   So if the value is 11 then the loop breaks. Also by default the value increased by 1. if you want to increase by 4 or 5.
    Code()                   Then need mention that in for loop

eg.
for i in range(1,11,2)      Here 1 is starting point of loop and 11 is breaking point of loop. now mentioned 2 is used to increase the number
    code()                  eg 1+2=3;3+2=5.......and so on
    code()
"""

# WAP print 1 to 10
for i in range(1, 11):
    print(i, end=(" "))

# WAP print the sequence 1,3,5,7....till 20
for i in range(1, 21, 2):
    print(i, end=(" "))

# WAP print 10 to 1
for i in range(10, 0, -1):
    print(i, end=(" "))


# Q42. Ask a number from user. Print all the numbers from 1 to that number.
num = int(input("Enter the Number = "))
num += 1
for i in range(1, num):
    print(i, end=(" "))


# Q43. Ask a number (N) from user. Print all the numbers from N to 1.
num = int(input("Enter the Number = "))
for num in range(num, 0, -1):
    print(num, end=(" "))

# Q44. Ask start number and end number from user. Print all the numbers from start to end using while loop.
num1 = int(input("Enter the Starting Number = "))
num2 = int(input("Enter the Ending Number = "))
num2 += 1
for num1 in range(num1, num2):
    print(num1, end=" ")

# Q45. Calculate the sum of all the numbers from 1 to 10.
sum = 0
for i in range(1, 11):
    sum = sum + i
print(f"Sum of all the numbers from 1 to 10 is = {sum}")

# Q46. Calculate product of all the numbers from 1 to 10.
prod = 1
for i in range(1, 11):
    prod = prod * i
print(f"Product of all the numbers from 1 to 10 is = {prod}")

# Q47. Calculate how many numbers are divisible by 7 from 1 to 100.
num = 0
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=(" "))
        num += 1
print(f"\nThere are total {num} in 1 to 100 which is divisible by 7.")


# Q48. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
num = 0
for i in range(1, 201):
    if i % 6 == 0 and i % 7 == 0:
        print(i, end=" ")
        num += 1
print(f"\nThere are total {num} in 1 to 200 which is divisible by both 6 and 7.")


# Q49. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.
sum = 0
for i in range(20, 51):
    if i % 4 == 0:
        sum = sum + i
print(f"The sum of all the numbers divisible by 4 from 20 to 50 is {sum}")

# Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.
div_6 = 0
div_7 = 0
div_6and7 = 0

for i in range(1, 200):
    if i % 6 == 0 and i % 7 == 0:
        div_6and7 += 1
    else:
        if i % 6 == 0:
            div_6 += 1
        elif i % 7 == 0:
            div_7 += 1
# div_6 = div_6 + div_6and7
# div_7 = div_7 + div_6and7
print(
    f"There are total {div_6} number which is divisible by 6 and total {div_7} number which is divisible by 7 and {div_6and7} number which is divisible by both."
)


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
for i in range(1, 11):
    prod = num * i
    print(f"{num} x {i} = {prod}")


"""
Q52. Calculate factorial of a number entered by user.
Example:
Enter a number = 5
Factorial of a number means product of all the numbers from 1 to that
number.
5 factorial = 5 x 4 x 3 x 2 x 1
Output = 120
"""
num = int(input("Enter the Number = "))
prod = 1
for num in range(num, 0, -1):
    prod = prod * num

print(f"Factorial is {prod}.")

# Q53. Ask to numbers x and y from the user. If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x.
a = x = int(input("Enter the value of x = "))
b = y = int(input("Enter the value of y = "))
a += 1
b += 1
if x < y:
    for x in range(x, b):
        print(x, end=(" "))
else:
    for y in range(y, a):
        print(y, end=(" "))
