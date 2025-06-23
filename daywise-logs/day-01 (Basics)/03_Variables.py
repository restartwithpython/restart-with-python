# Variable : It is like  container which used to store value of any data type

x = 5
y = 2
z = x - y
print(x)
print(y)
print(z)

name = "Tushar Mandali"
age = "22"
gender = "Male"
print(name, "\n", age, "\t", gender)

"""
DOCSTRING !!!
RULES OF VARIABLE :

1.Variable name must start with a letter or [_] underscore
2.Variable name can only contain numbers,letters and [_] underscore. Special characters or space is not valid.
3.Variable name are case sensitive. eg.{"myVar" and "myvar" are treated as two different variable}
4.Variable name should be meaningful and indicates the purpose of the variable
"""

first_name = "Tushar"
last_name = "Mandali"
print(first_name, last_name)

# Printing Variables in Different Ways

name = "Tushar Mandali"
age = "22"
gender = "Male"

print("My name is", name)
print("My age is", age)
print("My gender is", gender)

print("My name is", name, "My age is", age, "My gender is", gender)

# F-string Method
print(f"My name is {name} and I am {age} years old")

# Difference Between Concatination and F-string {https://stackoverflow.com/questions/59180574/string-concatenation-with-vs-f-string}
