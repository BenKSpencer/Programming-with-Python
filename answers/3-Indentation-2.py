# Lesson 3 in 'The Official Raspberry Pi Beginner's Guide' book
# To change the indentation from a definite range to an infinite range, we can use a 'while' loop instead of a 'for' loop
# Ensure each section is run separately using comments to avoid infinite loops

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
print("loop starting!") # This is not indented, so it runs before the loop.
while True: # While True is an infinite loop, it will run forever unless we break out of it.
    print("Checking the register...") # This is indented, so it runs inside the loop.
print("loop finished!") # This is not indented, so it runs after the loop. However, this line will never be reached because the loop above 
                       # is infinite and has no break statement.
                       
# 2. Add a second indented print() inside the loop. What pattern do you see?
print("loop starting!") # This is not indented, so it runs before the loop.
while True: # While True is an infinite loop, it will run forever unless we break out of it.
    print("Checking the register...") # This is indented, so it runs inside the loop.
    print("Checking the register again...") # This is also indented, so it runs inside the loop following the previous print() statement.
print("loop finished!")
# You will see the two messages printed repeatedly in the order they are written, as the loop runs indefinitely.

# 3. Indent print("loop finished!") so it is inside the loop. What happens
#    now, and why?
print("loop starting!") # This is not indented, so it runs before the loop.
while True: # While True is an infinite loop, it will run forever unless we break out of it.
    print("Checking the register...") # This is indented, so it runs inside the loop.
    print("Checking the register again...") # This is also indented, so it runs inside the loop following the previous print() statement.
    print("loop finished!") # This is indented, so it runs inside the loop. It will run forever
                            # unless we break out of the loop. The message "loop finished!" will
                            # print after every "Checking the register..." message.
# All three print() statements are indented, so they all run inside the loop. The loop will run indefinitely.

# 4. Change while True to while False. What happens, and why does
#    "loop finished!" now print?
print("loop starting!") # This is not indented, so it runs before the loop.
while False: # While False is a loop that will never run because the condition is always false.
    print("Checking the register...") # This is indented, so it would run inside the loop if the loop ran.
    print("Checking the register again...") # This is also indented, so it would run inside the loop following the previous print() statement if the loop ran.
print("loop finished!") # This is not indented, so it runs after the loop. Since the loop never runs, this line runs straight away.
# While false never runs the loop because the condition is always false, so the indented code block is skipped.

# 5. Lesson 1 showed that comparisons give True or False. Try while 1 > 2:
#    and then while 2 > 1:. Predict what each will do before you run it.
#    (Lesson 5 shows how to stop a loop on purpose with break.)
print("loop starting!") # This is not indented, so it runs before the loop.
while 1 > 2: # This condition is false, so the loop will never run.
    print("This will never print.") # This is indented, so it would run inside the loop if the loop ran. However, since the loop never runs, this line will not execute.
print("loop finished!") # This is not indented, so it runs after the loop. Since the loop never runs, this line will execute.

print("loop starting!") # This is not indented, so it runs before the loop.
while 2 > 1: # This condition is true, so the loop will run indefinitely.
    print("This will print forever.") # This is indented, so it runs inside the loop. It will run forever unless we break out of the loop.