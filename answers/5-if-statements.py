# Lesson 5 devised by Claude AI (Anthropic)
# if, elif and else: making decisions

# An if statement runs a block of code only when a condition is True.
# The condition uses the comparison operators from Lesson 1 (==, <, > ...).
# Like a loop, the code that belongs to the if statement is indented.

pcn_value = 73.09     # % of hypertension patients controlled in one PCN
england_value = 74.01  # the same figure for England

if pcn_value > england_value:
    print("This PCN is above England.")  # Only runs if the condition is True.

# else gives a block to run when the condition is False.

else:
    print("This PCN is not above England.")  # This one runs, because 73.09 is not > 74.01.

# elif means "else if". It checks another condition when the first is False.
# Python checks each condition from the top and runs only the FIRST block
# that is True. The rest are skipped.
difference = pcn_value - england_value
print(f"Difference from England: {difference:.2f} points")

if difference > 1:
    print("Well above England")
elif difference < -5:
    print("Far below England")
elif difference < -1:
    print("Well below England")
else:
    print("Similar to England")  # Runs, because -0.92 is between -1 and 1.

# Conditions can be combined with and, or and not (also from Lesson 1).
imd_decile = 3  # Index of Multiple Deprivation decile: 1 = most deprived, 10 = least

if imd_decile <= 3 and pcn_value < england_value:
    print("Deprived area that is below England: a possible inequality to look at.")

# if statements work well inside a for loop (Lesson 2). Here a loop
# checks every decile from 1 to 10.
for decile in range(1, 11):
    if decile <= 3:
        print(decile, ": more deprived", sep="") # sep="" means put nothing between the items
    elif decile <= 7:
        print(decile, ": middle", sep="") # sep="" means put nothing between the items
    else:
        print(decile, ": less deprived", sep="") # sep="" means put nothing between the items
# alternatively, we could use an f-string e.g print(f"{decile}: string")

# break stops a loop early. This fixes the infinite loop from Lesson 3:
# the while loop now has a way out.
count = 0
while True:
    count += 1  # or count = count + 1
    print("Loop running!", count)
    if count == 3:  # once it reaches 3, the new 'break' block runs
        break  # Leave the loop when count reaches 3.
print("loop finished!")  # This line is now reached.

# Try it yourself:
# 1. Change pcn_value to 76.5, then 72.0, and run the file each time.
# At 76.5, pcn_value is "above England" and so prints "Well above England"
# At 72.0, pcn_value is "below England" and so prints "Well below England"


# 2. Add a fourth category: "Far below England" when difference < -5.
#    Hint: the order of elif checks matters. Which should come first?
# The order of categories matters, the extreme conditions need to come before
# the broader ones.  For e.g below -5 is also below -1.  If < -1 came first
# any value below -5 would satisfy the <-1 condition and print "Well
# below England".