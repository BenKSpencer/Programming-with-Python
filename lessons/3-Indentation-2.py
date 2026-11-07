# Lesson 3 in 'The Official Raspberry Pi Beginner's Guide' book
# To change the indentation from a definite range to an infinite range, we can use a 'while' loop instead of a 'for' loop

print("loop starting!") # This is not indented, so it runs before the loops.
while True: # While True is an infinite loop, it will run forever unless we break out of it
    
    print("Loop running!") # This is indented, so it runs inside the loop. It will run forever
                           # unless we break out of the loop.

print("loop finished!") # This is not indented, so it runs after all the loops. However, 
                        # this line will never be reached because the loop above is infinite
                        # and has no break statement. 
