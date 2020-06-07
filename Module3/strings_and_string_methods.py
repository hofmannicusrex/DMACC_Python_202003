"""
Program: strings_and_string_methods.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/6/2020

Program specifications: The program will demonstrate different Python string methods.
"""
string_to_test = 'Aragorn in The Lord of the Rings'

# capitalize
print("---capitalize---")
print(str.capitalize(string_to_test))

# find | seems to return -1 if it can't find the sub
# It can't find the 'd' in this str.find("find", "d", 0, 2) because it's in the 3rd index.
print("\n---find---")
print(str.find(string_to_test, "s"))
print(str.find("find", "d", 0, 2))

# index
print("\n---index---")
print(str.index(string_to_test, "L"))
print(str.index("index", "x"))

# isalnum
print("\n---isalnum---")
print(str.isalnum(string_to_test))
print(str.isalnum("-"))

# isalpha
print("\n---isalpha---")
print(str.isalpha(string_to_test))
print(str.isalpha("NickHofmann"))

# isdigit
print("\n---isdigit---")
print(str.isdigit("900727530"))
print(str.isdigit(string_to_test))

# islower
print("\n---islower---")
print(str.islower(string_to_test))
print(str.islower("nick1"))

# isupper
print("\n---isupper---")
print(str.isupper("NICK1"))
print(str.isupper(string_to_test))

# isspace
print("\n---isspace---")
print(str.isspace(" "))
print(str.isspace(string_to_test))

# startswith
print("\n---startswith---")
print(string_to_test.startswith("Aragorn"))
print(string_to_test.startswith("ara"))
