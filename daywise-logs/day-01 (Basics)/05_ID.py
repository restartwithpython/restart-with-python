"""
id() function returns the unique memory address (identity) of an object.
Syntax = id(object)


Why it's useful:

To check if two variables point to the same object
Helpful in understanding mutable vs immutable types
Useful for debugging and optimization

"""

# Immutable types (int, str, bool):
a = 100
b = 100
print(id(a) == id(b))  # True (Python reuses memory for small values)

# Mutable types (list, dict, set):

x = [1, 2]
y = [1, 2]
print(id(x) == id(y))  # False (Different memory locations)

m = [1, 2]
n = m

print(id(m) == id(n))  #  True — both refer to the same object
