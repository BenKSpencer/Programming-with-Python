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
