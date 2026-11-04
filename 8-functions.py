# Lesson 8 devised by Claude AI (Anthropic)
# Functions: writing your own reusable commands

# You have already used built-in functions such as print(), len() and round().
# def lets you make your own. Code inside the function is indented and only
# runs when the function is called (used).

def say_hello():
    print("Hello from my function!")

say_hello()  # Calling the function runs the code inside it.
say_hello()  # It can be called as many times as you like.

# A function can take inputs, called parameters, inside the brackets.
def greet(name):
    print(f"Hello, {name}!")

greet("Ben")
greet("Coastal")

# return sends a value back out of the function, so you can store or print it.
# This function works out a percentage, a calculation used all the time in
# population health data.
def percentage(numerator, denominator):
    return numerator / denominator * 100

result = percentage(5010, 6855)
print(round(result, 1))                    # Prints 73.1
print(round(percentage(6515, 9200), 1))    # Prints 70.8

# Why use functions? You write the calculation once, give it a clear name,
# and if it needs fixing you fix it in one place.

# A function can protect against problems. Dividing by zero causes an error,
# so this version checks first.
def safe_percentage(numerator, denominator):
    if denominator == 0:
        return None  # None means "no value".
    return round(numerator / denominator * 100, 1)

print(safe_percentage(10, 0))   # Prints None instead of crashing.
print(safe_percentage(10, 40))  # Prints 25.0

# A function can use if statements to sort a value into a category.
def compare_to_england(value, england=74.01):
    # england=74.01 is a default value. It is used if you do not give one.
    difference = value - england
    if difference > 1:
        return "Above England"
    elif difference < -1:
        return "Below England"
    else:
        return "Similar to England"

print(compare_to_england(73.09))         # Similar to England
print(compare_to_england(69.62))         # Below England
print(compare_to_england(80, england=85))  # Uses 85 instead: Below England

# A function can take a list and loop through it.
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([7650, 3420, 3580, 6810]))  # Prints 5365.0

# Putting it together: a list of dictionaries (Lesson 7) and our functions.
pcns = [
    {"PCN": "Dogwood PCN", "Numerator": 5010, "Denominator": 6855},
    {"PCN": "Hazel PCN", "Numerator": 6515, "Denominator": 9200},
    {"PCN": "Hornbeam PCN", "Numerator": 4430, "Denominator": 6405},
]

for row in pcns:
    value = safe_percentage(row["Numerator"], row["Denominator"])
    print(f"{row['PCN']}: {value}% - {compare_to_england(value)}")

# Try it yourself:
# 1. Write a function called imd_group(decile) that returns "More deprived"
#    for deciles 1 to 3, "Middle" for 4 to 7 and "Less deprived" for 8 to 10.
# 2. Call it with a few deciles and print the results.
