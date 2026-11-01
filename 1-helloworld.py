# Lesson 1 in 'The Official Raspberry Pi Beginner's Guide'

# print() is a built-in function. It displays the value you put inside its
# parentheses in the console.
print("hello world!")

# Text in quotes is called a string. Strings can use double or single quotes.
print('hello world!')

# Numbers do not need quotes. An integer is a whole number, while a float
# is a number that has a decimal point.
print(1)
print(1.5)

# Boolean values represent one of two truth values: True or False.
print(True)
print(False)

# Arithmetic operators let you perform calculations with numbers.
print(1 + 1)   # + adds numbers.
print(2 * 3)   # * multiplies numbers.
print(10 / 2)  # / divides numbers; in Python 3 this gives 5.0.
print(10 - 2)  # - subtracts the number on the right from the number on the left.
print(2 ** 3)  # ** raises the left number to the power of the right number.
print(10 % 3)  # % gives the remainder after division: 1.

# Comparison operators compare two values and produce a Boolean result.
print(1 == 1)  # == checks whether the values are equal.
print(1 != 2)  # != checks whether the values are not equal.
print(1 < 2)   # < checks whether the left value is less than the right.
print(2 > 1)   # > checks whether the left value is greater than the right.
print(1 <= 1)  # <= checks whether the left value is less than or equal to the right.
print(2 >= 1)  # >= checks whether the left value is greater than or equal to the right.

# The logical operators and, or, and not combine or reverse Boolean values.
print(True and False)  # and is True only when both values are True.
print(True or False)   # or is True when at least one value is True.
print(not True)        # not reverses the Boolean value.

# The + and * operators also work with strings: + joins strings, and *
# repeats a string.
print("hello" + " " + "world!")
print("hello" * 3)
print("hello" * 3 + " " + "world!")  # String operators can be combined.

# len() is a built-in function. It returns the number of items in a value;
# for a string, that means the number of characters.
print(len("hello world!"))  # The result is 12 and includes spaces and punctuation.

# String methods are functions associated with strings. The string before
# the dot is the value the method works on.
print("hello world!".upper())  # .upper() returns an uppercase version. The result is "HELLO WORLD!"
print("hello world!".lower())  # .lower() returns a lowercase version. The result is "hello world!"
print("hello world!".title())  # .title() capitalizes the words. The result is "Hello World!"
print("hello world!".replace("world", "Python"))  # .replace() substitutes text.

# String formatting puts values into a string. .format() is a string method;
# an f-string is another formatting feature, not a function or method.
print("Hello, {}!".format("World"))  # {} is a placeholder for a value. The result is "Hello, World!".
print("Hello, {name}!".format(name="World"))  # A placeholder can be named. The result is "Hello, World!".
print(f"Hello, {'World'}!")  # Expressions inside {} are evaluated.
print(f"Hello, {'World'}! The length is {len('World')}.")
