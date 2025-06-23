# Escape Sequences : It is an illegal characters which allows code to run without executing this charachter.
# It is always used in Print Statement
# Eg. when we use backshash "\" it allows program to escape the next characters
"""
DOCSTRING !!

\' : Single Quotation
\" : Double Quotation
\\ : Backslash
\n : New Line
\t : Tab  (In TAB we skip 4 spaces "    ")
\b : Backspace
"""

print(
    "Hello World.\nCurrently I am currenly working in MNC."
)  # "\n" we used for new line
print("My CTC is \t\t\t jane do chodo.")  # "\t" we used for TAB
print(
    "I travel to office by \"Bus\" or with 'Friends'."
)  # "\'" and "\"" is used when we want double quotes in line
print("My Office workload  is v\\ery Ba\\d")


#                                   !!! ASSIGNMENT !!!

"""
Q1. Write a program that prints a path like this:
C:\\Users\\John\\Desktop\\File.txt using the appropriate escape sequences.
"""
print("C:\\Users\\John\\Desktop\\File.txt")

"""
Q2. Write a Python program that prints a message with a double-quote
character inside it.
For example: He said, "Hello!".
"""

print('He said, "Hello!".')

"""
Q3. Create a program that prints a message containing both single and
double quotes, like this: She said, 'It's cold'
"""

print("She said, 'It's cold\nShe said, \"It's cold\"")
