# Programming with Python

Hello! I'm new to Python, and this repository is where I'm keeping the code I write as I learn it.

## Where I'm starting

I started with **Chapter 5 – Programming with Python** of *The Official Raspberry Pi Beginner's Guide: How to use your new computer* by Gareth Halfacree (published by Raspberry Pi, [raspberrypi.org](https://www.raspberrypi.org)). Lessons 1–3 come from the book.

From Lesson 4, I'm following a lesson plan devised with Claude AI (Anthropic). It builds the Python basics I need for working with data, using population health examples. I can still return to the book's later exercises (such as turtle graphics) for fun.

Each lesson is saved as its own numbered script with plain-English comments, so I can look back and see how I've progressed.

## Why I'm learning

- **To learn Python and have fun doing it.** I want to build things, experiment, break things and work out how to fix them.
- **To use it in my job.** I work in informatics, and I'd like to learn how Python can help with **data and population health insights**, for example:
  - cleaning, joining and reshaping datasets
  - automating repetitive reporting tasks
  - analysing trends and differences between population groups
  - creating clear charts and visualisations to share findings
  - making analysis reproducible, so it can be re-run and checked

## Lesson plan

### Stage 1: Python basics (from the book)

| # | Script | What I learned | Status |
|---|--------|----------------|--------|
| 1 | [1-helloworld.py](1-helloworld.py) | `print()`, strings, numbers, Booleans, operators, string methods and f-strings | Done |
| 2 | [2-Indentation.py](2-Indentation.py) | `for` loops with `range()`, and how indentation defines a block of code | Done |
| 3 | [3-Indentation-2.py](3-Indentation-2.py) | `while True` loops, which run forever (press `Ctrl+C` to stop) | Done |

### Stage 2: The basics I need for data (devised by Claude AI, Anthropic)

| # | Script | What I'll learn | Status |
|---|--------|-----------------|--------|
| 4 | [4-variables.py](4-variables.py) | Variables, calculating a percentage, `round()`, converting text to numbers | Done |
| 5 | [5-if-statements.py](5-if-statements.py) | `if`, `elif` and `else`: comparing a PCN with England; `break` to fix Lesson 3's endless loop | To do |
| 6 | [6-lists.py](6-lists.py) | Lists: storing many values, `sum()`, `min()`, `max()`, averages, sorting and filtering | To do |
| 7 | [7-dictionaries.py](7-dictionaries.py) | Dictionaries: a row of data with labelled columns; a list of dictionaries as a table | To do |
| 8 | [8-functions.py](8-functions.py) | Writing my own functions, such as a reusable `percentage()` | To do |
| 9 | [9-reading-a-csv.py](9-reading-a-csv.py) | Reading a real CSV file of GP practices with the `csv` module | To do |

### Stage 3: Working with data using pandas (coming next)

| # | Topic | What I'll learn |
|---|-------|-----------------|
| 10 | Installing pandas and loading a CSV | `pip install`, `pd.read_csv()`, `.head()`, `.shape`, `.columns` |
| 11 | Selecting and filtering | Choosing columns, and keeping only the rows I need (e.g. one Locality) |
| 12 | Sorting and ranking | Finding the highest and lowest PCNs |
| 13 | New columns | Calculating percentages and differences from England |
| 14 | Grouping and summarising | Totals and averages by Locality with `.groupby()` |
| 15 | Joining tables | Combining practice data with PCN data using `.merge()` |
| 16 | My first chart | A bar chart with `matplotlib` |
| 17 | Mini project | Hypertension control by PCN compared with England, with a chart |

## Practice data

The [data/](data/) folder holds small practice datasets for learning. They are **fictional**: they're based on the shape of open CVDPREVENT data, but every name is made up and every number has been changed, so they don't describe any real practice, PCN or area.

- **ICBs** are named after animal groups: Fish ICB, Bird ICB and Insect ICB.
- **GP practices** are named after a species from their ICB's group, such as Salmon Health Centre, Blue Tit Practice or Ladybird Medical Centre.
- **PCNs** are named after trees, such as Oak PCN.
- **Localities** are named after landscapes: Coastal, Lakeside, Riverside, Woodland, Heathland and Meadow.
- **The numbers are scrambled:** list sizes, IMD deciles and hypertension figures are randomly adjusted, but kept realistic.

| File | Rows | What's in it |
|------|------|--------------|
| [practices_small.csv](data/practices_small.csv) | 10 | Ten GP practices in the Coastal locality: PCN, Locality, ICB, list size, IMD decile |
| [practices_all.csv](data/practices_all.csv) | 209 | The same columns for every practice in all six localities |
| [hypertension_by_pcn.csv](data/hypertension_by_pcn.csv) | 59 | Hypertension patients with blood pressure controlled, by PCN, to March 2026 (England: 74.01%) |

IMD decile: 1 = most deprived, 10 = least deprived.

## Running the scripts

You need Python 3 installed. The book uses the Thonny editor on a Raspberry Pi, but any Python 3 setup works. Run the scripts from this folder, so they can find the `data` folder:

```bash
python 4-variables.py
```

Each Claude lesson ends with a **Try it yourself** section with small exercises to type in.
