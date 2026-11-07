# Lesson 2 in 'The Official Raspberry Pi Beginner's Guide' book

# Indentation groups code into a block. The indented code under a for loop
# belongs to the loop and runs once for each value in the sequence.

print("loop starting!")  # This is not indented, so it runs before the loops.

# A for loop assigns each value in turn to its loop variable. The variable
# name can be any valid name; here, number takes the values 0 through 9.
for number in range(10):
    print("loop number:", number)

# range() variations
# range(stop) starts at 0 and counts up by 1, stopping before stop.
for number in range(5):
    print("loop number:", number)  # Prints 0, 1, 2, 3, 4.

# range(start, stop) starts at start and counts up by 1, stopping before stop.
for number in range(1, 11):
    print("loop number:", number)  # Prints 1 through 10.

# range(start, stop, step) also lets you choose how much to count by.
for number in range(2, 11, 2):
    print("counting up by 2:", number)  # Prints 2, 4, 6, 8, 10.

# A negative step counts down. The stop value is still excluded.
for number in range(10, 0, -1):
    print("counting down:", number)  # Prints 10 down to 1.

print("loop finished!")  # This is not indented, so it runs after all the loops.

# Try it yourself (added by Claude AI, Anthropic):
# 1. Print "Q1", "Q2", "Q3" and "Q4" using range() and an f-string.
#    Hint: f"Q{number}".
# 2. Print every year from 2020 to 2026. Check that 2026 is included.
# 3. Print the IMD deciles 1 to 10, then count back down from 10 to 1.
# 4. Print ages from 40 to 75 in steps of 5.
# 5. A gainshare pays £15 per patient each quarter. For quarters 1 to 4,
#    print the running total for one patient, e.g. "Quarter 2: £30".
#    Hint: multiply the loop variable by 15.
# 6. Remove the indentation from a print() inside one of your loops and
#    run the file. What error do you get, and what does it tell you?
