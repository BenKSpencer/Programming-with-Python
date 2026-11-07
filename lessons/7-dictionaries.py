# Lesson 7 devised by Claude AI (Anthropic)
# Dictionaries: storing values with labels

# In Lesson 6, two separate lists held practice names and list sizes.
# A dictionary keeps related values together, each one with a label.
# It uses curly brackets { }. Each item is a key (the label) and a value,
# joined by a colon.
practice = {
    "Practice": "Salmon Surgery",
    "PCN": "Medlar PCN",
    "Locality": "Coastal",
    "List_Size": 7650,
    "IMD_Decile": 9,
}

print(practice)

# Look up a value using its key in square brackets.
print(practice["Practice"])   # Prints Salmon Surgery
print(practice["List_Size"])  # Prints 7650

# A dictionary is like one row of a spreadsheet: the keys are the column
# headings and the values are the cells.
print(f"{practice['Practice']} is in {practice['Locality']} "
      f"and has {practice['List_Size']} patients.")
# Note: inside an f-string with double quotes, use single quotes for the key.

# Change a value, or add a new key, using =
practice["List_Size"] = 7900
practice["ICB"] = "Fish ICB"
print(practice)

# .keys() gives the labels, .values() gives the values.
print(practice.keys())
print(practice.values())

# .items() gives each key and value together, which is handy in a loop.
for key, value in practice.items():
    print(key, "=", value)

# A LIST of dictionaries is like a whole table: one dictionary per row.
# This is how data often looks once it is read from a CSV file (Lesson 9).
practices = [
    {"Practice": "Salmon Surgery", "Locality": "Coastal", "List_Size": 7650, "IMD_Decile": 9},
    {"Practice": "Trout Practice", "Locality": "Coastal", "List_Size": 3420, "IMD_Decile": 7},
    {"Practice": "Pike Medical Centre", "Locality": "Coastal", "List_Size": 3580, "IMD_Decile": 4},
    {"Practice": "Minnow Practice", "Locality": "Coastal", "List_Size": 16230, "IMD_Decile": 3},
]

# Loop through the rows and print one column.
for row in practices:
    print(row["Practice"])

# Add up one column: the total patients across all rows.
total = 0
for row in practices:
    total += row["List_Size"]
print("Total patients:", total)  # Prints 30880

# Filter rows: only practices in the more deprived half (deciles 1 to 5).
for row in practices:
    if row["IMD_Decile"] <= 5:
        print(f"{row['Practice']} (decile {row['IMD_Decile']})")

# A dictionary can also count things. Here we count practices per decile.
counts = {}
for row in practices:
    decile = row["IMD_Decile"]
    if decile in counts:
        counts[decile] += 1
    else:
        counts[decile] = 1
print(counts)

# Try it yourself:
# 1. Add a fifth practice to the practices list.
# 2. Work out the average list size of the four (or five) practices.
# 3. Print the name of the practice with the largest list size.
#    Hint: keep a variable for the biggest so far, and update it in the loop.
