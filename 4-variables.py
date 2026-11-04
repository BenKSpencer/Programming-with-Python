# Lesson 4 devised by Claude AI (Anthropic)
# Variables: giving a value a name so you can use it again later

# A variable is a labelled box that holds a value. The = sign puts the value
# on the right into the box named on the left. It does not mean "equals".
practice_name = "Salmon Surgery"
list_size = 7650

# You can print a variable just like a value. Python prints what is inside it.
print(practice_name)  # Prints Salmon Surgery
print(list_size)      # Prints 7650

# Variable names can use letters, numbers and underscores, but cannot start
# with a number or contain spaces. Use names that describe what they hold.

# Variables can be used in calculations. This is where they become useful.
# Example: how many patients with hypertension have their blood pressure
# controlled? (These numbers are for one PCN.)
numerator = 5010    # patients whose blood pressure is controlled
denominator = 6855  # all patients on the hypertension register

percentage = numerator / denominator * 100
print(percentage)  # Prints 73.08533916849015, which is too many decimal places

# round() is a built-in function. round(value, 1) keeps 1 decimal place.
print(round(percentage, 1))  # Prints 73.1

# An f-string (from Lesson 1) can put variables into a sentence.
print(f"{numerator} of {denominator} patients are controlled ({percentage:.1f}%).")
# :.1f inside the {} means "show this number with 1 decimal place".

# A variable can be changed. The new value replaces the old one.
list_size = 7700
print(f"{practice_name} now has {list_size} patients.")

# A variable can be updated using its own value.
list_size = list_size + 100  # Take the old value, add 100, store it back.
print(list_size)             # Prints 7800
list_size += 100             # += is a shortcut for the line above.
print(list_size)             # Prints 7900

# type() is a built-in function. It tells you what kind of value is inside.
print(type(practice_name))  # <class 'str'>   - a string (text)
print(type(list_size))      # <class 'int'>   - an integer (whole number)
print(type(percentage))     # <class 'float'> - a float (decimal number)

# Converting between types matters with data, because numbers read from a
# file arrive as text. int() and float() turn text into numbers.
list_size_text = "7650"
print(list_size_text + "1")       # Joins text: prints 76501
print(int(list_size_text) + 1)    # Adds numbers: prints 7651
print(float("73.09"))             # Prints 73.09 as a number

# Try it yourself:
# 1. Make variables for the England hypertension figure: 74.01
# 2. Work out the difference between percentage and the England figure.
# 3. Print a sentence like "This PCN is 0.7 points below England."

england_percentage = 74.01
difference = percentage - england_percentage
print(f"{practice_name} is {difference:.1f}% points below England.") 