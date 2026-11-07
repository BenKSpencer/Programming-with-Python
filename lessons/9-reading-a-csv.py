# Lesson 9 devised by Claude AI (Anthropic)
# Reading a CSV file: using real data for the first time

# A CSV (comma-separated values) file is a plain text table. The first line
# holds the column headings, and each line after that is one row.
# data/practices_small.csv holds 10 GP practices in the Coastal locality.
# Open it in VS Code first to see what it looks like inside.

# Run this file from the Programming-with-Python folder so Python can
# find the data folder.

# import loads a module: extra tools that come with Python but are not
# switched on until you ask. The csv module knows how to read CSV files.
import csv

# open() opens a file. with ... as file: closes it again automatically
# when the indented block finishes.
with open("data/practices_small.csv", encoding="utf-8") as file:
    # csv.DictReader turns each row into a dictionary (Lesson 7), using the
    # column headings as the keys.
    reader = csv.DictReader(file)
    practices = list(reader)  # Store all the rows in a list.

# practices is now a list of dictionaries, one per practice.
print("Number of rows:", len(practices))  # Prints 10
print("First row:", practices[0])

# Print one column from every row.
for row in practices:
    print(row["Practice"])

# IMPORTANT: everything read from a CSV arrives as text (a string), even
# numbers. "8855" is text, so you must convert it with int() (Lesson 4)
# before doing maths.
print(type(practices[0]["List_Size"]))  # <class 'str'>

total = 0
for row in practices:
    total += int(row["List_Size"])
print(f"Total patients across {len(practices)} practices: {total}")
print(f"Average list size: {total / len(practices):.0f}")

# Find the largest practice.
largest = practices[0]
for row in practices:
    if int(row["List_Size"]) > int(largest["List_Size"]):
        largest = row
print(f"Largest practice: {largest['Practice']} ({largest['List_Size']} patients)")

# Filter: practices in the more deprived half (IMD deciles 1 to 5).
print("Practices in IMD deciles 1-5:")
for row in practices:
    if int(row["IMD_Decile"]) <= 5:
        print(f"  {row['Practice']} - decile {row['IMD_Decile']}")

# Count practices per PCN using a dictionary (Lesson 7).
pcn_counts = {}
for row in practices:
    pcn = row["PCN"]
    pcn_counts[pcn] = pcn_counts.get(pcn, 0) + 1
    # .get(pcn, 0) gives the current count, or 0 if this PCN is new.
for pcn, count in pcn_counts.items():
    print(f"{pcn}: {count} practice(s)")

# Try it yourself:
# 1. Change the file name to "data/practices_all.csv" (209 practices across
#    all the localities) and run it again. Does everything still work?
# 2. Count how many practices there are in each Locality.
# 3. Work out the total list size for each Locality.
#    Hint: a dictionary where the key is the Locality and the value is a total.
#
# Notice how much code this takes. In the next lessons, the pandas library
# will do each of these jobs in one line, but you now know what it is doing
# behind the scenes.
