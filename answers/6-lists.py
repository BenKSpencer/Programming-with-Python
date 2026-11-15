# Lesson 6 devised by Claude AI (Anthropic)
# Lists: storing many values in one variable

# A list holds several values in order, inside square brackets [ ].
# The values are separated by commas.
practices = ["Salmon Surgery", "Trout Practice", "Pike Medical Centre", "Perch Health Centre"]
list_sizes = [7650, 3420, 3580, 6810]

print(practices)
print(list_sizes)

# len() (from Lesson 1) also counts the items in a list.
print(len(practices))  # Prints 4

# Each item has a position number called an index. Indexes start at 0, not 1.
print(practices[0])   # Prints Salmon Surgery (the first item)
print(practices[1])   # Prints Trout Practice (the second item)
print(practices[-1])  # A negative index counts from the end: Perch Health Centre

# A for loop (Lesson 2) can go through a list one item at a time.
for practice in practices:
    print("Practice:", practice)

# enumerate() adds a counter to a for loop. It gives two values each time:
# the count, then the item. start=1 makes the count begin at 1 instead of 0.
for number, practice in enumerate(practices, start=1):
    print(f"{number}. {practice}")  # Prints 1. Salmon Surgery, 2. Trout Practice, ...

# Built-in functions for lists of numbers.
print(sum(list_sizes))  # Adds them all up: 21460
print(min(list_sizes))  # The smallest: 3420
print(max(list_sizes))  # The largest: 7650

# There is no built-in average, but you can make one from sum() and len().
average = sum(list_sizes) / len(list_sizes)
print(f"Average list size: {average:.0f} patients")  # :.0f means no decimal places.

# .append() adds an item to the end of a list.
practices.append("Carp Surgery")
list_sizes.append(14120)
print(practices)

# sorted() returns a sorted copy of the list. The original is unchanged.
print(sorted(list_sizes))                # Smallest to largest
print(sorted(list_sizes, reverse=True))  # Largest to smallest
print(sorted(practices))                 # Alphabetical order

# in checks whether a value is in a list. It gives True or False.
print("Salmon Surgery" in practices)    # True
print("Cod Surgery" in practices)  # False

# A loop with an if statement (Lesson 5) can pick out some values.
# Here we count and collect the small practices.
small_practices = []  # An empty list to fill up.
for size in list_sizes:
    if size < 5000:
        small_practices.append(size)
print("List sizes under 5,000:", small_practices)
print("Number of small practices:", len(small_practices))

# zip() pairs up two lists, so you can loop through both together.
for practice, size in zip(practices, list_sizes):
    print(f"{practice}: {size} patients")

# Try it yourself:
# 1. Add another practice and list size, then check the total again.
practices.append("Cod Surgery")
list_sizes.append(12567)
for practice, size in zip(practices, list_sizes):
    print(f"{practice}: {size}")
print(sum(list_sizes))
# 2. Make a list called imd_deciles with the values 9, 7, 4, 6, 5, 3
#    (one for each practice, in the same order, including the one you added).
imd_deciles=[9,7,4,6,5,3]
#    Print how many practices are in deciles 1 to 5 (more deprived half).
deprived_list = [] # will hold the deciles that are 1 to 5.
for imd in imd_deciles:
    if imd <=5:
        deprived_list.append(imd)
print("number of practices in deciles 1 to 5 (more deprived half):",len(deprived_list))
# 3. Use zip() to print each practice with its decile, for example
#    Salmon Surgery: decile 9. Check that all six practices appear.
for practice, imd in zip(practices, imd_deciles):
    print(f"{practice} has a decile of {imd}")