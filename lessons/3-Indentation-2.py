# Lesson 3 in 'The Official Raspberry Pi Beginner's Guide' book
# To change the indentation from a definite range to an infinite range, we can use a 'while' loop instead of a 'for' loop

print("loop starting!") # This is not indented, so it runs before the loops.
while True: # While True is an infinite loop, it will run forever unless we break out of it
    
    print("Loop running!") # This is indented, so it runs inside the loop. It will run forever
                           # unless we break out of the loop.

print("loop finished!") # This is not indented, so it runs after all the loops. However, 
                        # this line will never be reached because the loop above is infinite
                        # and has no break statement.

# Try it yourself (added by Claude AI, Anthropic):
# 1. Change the message inside the loop to "Checking the register..." and
#    run it. Stop it with Ctrl+C.
# 2. Add a second indented print() inside the loop. What pattern do you see?
# 3. Indent print("loop finished!") so it is inside the loop. What happens
#    now, and why?
# 4. Change while True to while False. What happens, and why does
#    "loop finished!" now print?
# 5. Lesson 1 showed that comparisons give True or False. Try while 1 > 2:
#    and then while 2 > 1:. Predict what each will do before you run it.
#    (Lesson 5 shows how to stop a loop on purpose with break.)
