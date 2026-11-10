# Lesson 2 in 'The Official Raspberry Pi Beginner's Guide' book

# Indentation groups code into a block. The indented code under a for loop
# belongs to the loop and runs once for each value in the sequence.

print("loop starting!")  # This is not indented, so it runs before the loops.

# A for loop assigns each value in turn to its loop variable. The variable
# name can be any valid name; here, number takes the values 0 through 9.
# range(10) is a built-in function that makes a sequence of numbers e.g range(10) makes 0, 1, 2....9, but not 10.
for number in range(10):  # The colon (:) starts the indented block of code that belongs to the loop.
    print("loop number:", number) # The identaton shows this line belongs to the loop.

# range() variations
# range(stop) starts at 0 (if not specified) and counts up by 1 (if not specified), stopping before stop value..
for number in range(5):
    print("loop number:", number)  # Prints "loop number: 0", "loop number: 1", etc.

# range(start, stop) starts at start value (as specified by start) and counts up by 1 (if not specified), stopping before stop value.
for number in range(1, 11):
    print("loop number:", number)  # Prints 1 through 10.

# range(start, stop, step) starts at start value (as specified by start) and counts up by 2 (as specified by step), stopping before stop value.
for number in range(2, 11, 2):
    print("counting up by 2:", number)  # Prints 2, 4, 6, 8, 10.

# A negative step counts down. The stop value is still excluded.
for number in range(10, 0, -1):
    print("counting down:", number)  # Prints 10 down to 1.

print("loop finished!")  # This is not indented, so it runs after all the loops.

# Try it yourself (added by Claude AI, Anthropic):
# 1. Print "Q1", "Q2", "Q3" and "Q4" using range() and an f-string.
#    Hint: f"Q{number}".
for number in range(1,5): # The range() function generates numbers from 1 to 4 (5 is excluded as it's the stop value). : starts the indented block of code that belongs to the loop.
    print(f"Q{number}") # The indentation shows this line belongs to the loop. It prints "Q" followed by the value of number for each iteration of the loop.

# 2. Print every year from 2020 to 2026. Check that 2026 is included.
for year in range(2020, 2027): # The range() function generates numbers from 2020 to 2026 (2027 is excluded as it's the stop value).
    print(year) # The indentation shows this line belongs to the loop. It prints the value of year for each iteration of the loop.

# 3. Print the IMD deciles 1 to 10, then count back down from 10 to 1.

for imd in range(1, 11): # The range() function generates numbers from 1 to 10 (11 is excluded as it's the stop value).
    print(imd) # Prints the value of imd for each iteration of the loop.
for imd in range(10, 0, -1): # The range() function generates numbers from 10 to 1 (0 is excluded as it's the stop value).
    print(imd) # Prints the value of imd for each iteration of the loop.

# 4. Print ages from 40 to 75 in steps of 5.
for age in range(40, 76, 5): # The range() function generates numbers from 40 to 75 (76 is excluded as it's the stop value) in steps of 5.
    print(age) # Prints the value of age for each iteration of the loop.

# 5. A gainshare pays £15 per patient each quarter. For quarters 1 to 4,
#    print the running total for one patient, e.g. "Quarter 2: £30".
#    Hint: multiply the loop variable by 15.
for gainshare in range(1, 5): # The range() function generates numbers from 1 to 4 (5 is excluded as it's the stop value).
    print(f"Quarter {gainshare}: £{gainshare * 15}") # Prints the "Quarter" followed by the value of gainshare (1 to 4) then £ followed by the gainshare value multiplied by 15 for each iteration of the loop.

# 6. Remove the indentation from a print() inside one of your loops and
#    run the file. What error do you get, and what does it tell you?
#    IndentationError: expected an indented block after 'for' statement on line 57. 
#    This error occurs because Python expects an indented block of code to follow the 'for' statement, indicating which lines of code belong to the loop. 
#    Without indentation, Python cannot determine which statements are part of the loop, leading to a syntax error.