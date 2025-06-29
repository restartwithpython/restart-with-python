"""
WAP to print the following statement
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=(" "))
    print()

"""
WAP to print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=(" "))
    print()

"""
WAP to print the following pattern 
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=(" "))
    print()


"""
WAP to print the following pattern 
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end=(" "))
    print()

"""
WAP to print the following pattern 
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(i, end=(" "))
    print()


"""
WAP to print the following pattern 
*
* *
* * *
* * * *
* * * * *
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

"""
WAP to print the following pattern 
5 4 3 2 1
5 4 3 2
5 4 3
5 4 
5
"""

for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end=(" "))
    print()

"""
WAP to print the following pattern 
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(i, end=(" "))
    print()

"""
WAP to print the following pattern 
* * * * *
* * * * 
* * *
* *
*
"""

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end=(" "))
    print()

"""
WAP to print the following pattern 
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=(" "))
    print()

"""
WAP to print the following pattern 
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(i, end=" ")
    print()

"""
WAP to print the following pattern 
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

"""
WAP to print the following pattern 
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=(" "))
    print()

"""
WAP to print the following pattern 
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
sum = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(sum, end=" ")
        sum = sum + 1
    print()


"""
WAP to print the following pattern 
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=(" "))
    print()
"""
WAP a program to print below pattern 
        *
      * *
    * * *
  * * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=(" "))
    for k in range(1, i + 1):
        print("*", end=" ")
    print()


"""
WAP a program to print below pattern 
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=(" "))
    print()


"""
WAP a program to print below pattern 
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(i, end=(" "))
    print()

"""
WAP a program to print below pattern 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=(" "))
    print()


"""
WAP a program to print below pattern 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=" ")
    print()

"""
WAP a program to print below pattern 

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()


"""
WAP a program to print below pattern 

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

for i in range(5, 1, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=(" "))
    print()
