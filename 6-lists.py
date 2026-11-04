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
# 2. Make a list called imd_deciles with the values 9, 7, 4, 6, 5.
#    Print how many practices are in deciles 1 to 5 (more deprived half).
