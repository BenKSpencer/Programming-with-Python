# Programming with Python

Hello! I'm new to Python, and this repository is where I'm keeping the code I write as I learn it.

## Where I'm starting

I started with **Chapter 5 – Programming with Python** of *The Official Raspberry Pi Beginner's Guide: How to use your new computer* by Gareth Halfacree (published by Raspberry Pi, [raspberrypi.org](https://www.raspberrypi.org)). Lessons 1–3 come from the book, with **Try it yourself** exercises added by Claude AI (Anthropic) so every lesson has questions to answer.

From Lesson 4, I'm following a lesson plan devised with Claude AI (Anthropic). It builds the Python basics I need for working with data, using population health examples. I can still return to the book's later exercises (such as turtle graphics) for fun.

## Where I'm heading

The goal is to go beyond Python itself and learn the skills behind NHS data and population health work: how data is **stored** (SQL), **shared** between systems (APIs, FHIR and clinical codes, as used in Shared Care Records), **analysed** fairly (rates, confidence intervals, funnel plots and inequality gaps) and **shared** with others (notebooks, dashboards and automated reports). The plan runs from Lesson 1 to Lesson 46 and ends with a capstone project on medicines and health inequalities.

Each lesson is saved as its own numbered script with plain-English comments, so I can look back and see how I've progressed.

## How the repository is organised

| Folder | What's in it |
|--------|--------------|
| [lessons/](lessons/) | The lessons, kept clean with their **Try it yourself** questions unanswered, so anyone can use them |
| [answers/](answers/) | My worked copy of each lesson, including my answers to **Try it yourself** |
| [data/](data/) | Fictional practice datasets used by the lessons |

For each lesson I create a branch, copy the lesson into `answers/`, work through it there, then merge the branch into `main`.

## Why I'm learning

- **To learn Python and have fun doing it.** I want to build things, experiment, break things and work out how to fix them.
- **To use it in my job.** I work in informatics, and I'd like to learn how Python can help with **data and population health insights**, for example:
  - cleaning, joining and reshaping datasets
  - automating repetitive reporting tasks
  - analysing trends and differences between population groups
  - querying databases with SQL and pulling open NHS data from APIs
  - understanding how health systems exchange data (FHIR, SNOMED CT, dm+d)
  - measuring inequalities with sound population health methods
  - creating clear charts and visualisations to share findings
  - making analysis reproducible, so it can be re-run and checked

## Lesson plan

### Stage 1: Python basics (from the book, with exercises by Claude AI)

| # | Script | What I'll learn | Status |
|---|--------|----------------|--------|
| 1 | [1-helloworld.py](lessons/1-helloworld.py) | `print()`, strings, numbers, Booleans, operators, string methods and f-strings | Done ([my answers](answers/1-helloworld.py)) |
| 2 | [2-Indentation.py](lessons/2-Indentation.py) | `for` loops with `range()`, and how indentation defines a block of code | Done ([my answers](answers/2-Indentation.py)) |
| 3 | [3-Indentation-2.py](lessons/3-Indentation-2.py) | `while True` loops, which run forever (press `Ctrl+C` to stop) | Done ([my answers](answers/3-Indentation-2.py)) |

### Stage 2: The basics I need for data (devised by Claude AI, Anthropic)

| # | Script | What I'll learn | Status |
|---|--------|-----------------|--------|
| 4 | [4-variables.py](lessons/4-variables.py) | Variables, calculating a percentage, `round()`, converting text to numbers | Done ([my answers](answers/4-variables.py)) |
| 5 | [5-if-statements.py](lessons/5-if-statements.py) | `if`, `elif` and `else`: comparing a PCN with England; `break` to fix Lesson 3's endless loop | Done ([my answer](answers/5-if-statements.py)) |
| 6 | [6-lists.py](lessons/6-lists.py) | Lists: storing many values, `sum()`, `min()`, `max()`, averages, sorting and filtering | To do |
| 7 | [7-dictionaries.py](lessons/7-dictionaries.py) | Dictionaries: a row of data with labelled columns; a list of dictionaries as a table | To do |
| 8 | [8-functions.py](lessons/8-functions.py) | Writing my own functions, such as a reusable `percentage()` | To do |
| 9 | [9-reading-a-csv.py](lessons/9-reading-a-csv.py) | Reading a real CSV file of GP practices with the `csv` module | To do |

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

### Stage 4: SQL (planned)

| # | Topic | What I'll learn |
|---|-------|-----------------|
| 18 | CSV to database | `sqlite3`, `df.to_sql()`, tables, rows and primary keys |
| 19 | SELECT and WHERE | Choosing columns, filtering rows, `AND`/`OR`, `LIKE` |
| 20 | Sorting and limits | `ORDER BY`, `LIMIT`, `DISTINCT` |
| 21 | Aggregating | `COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING` |
| 22 | Joins | `INNER` and `LEFT JOIN`, and why rows go missing or duplicate |
| 23 | Building up a query | `CASE WHEN`, subqueries and CTEs (`WITH`) |
| 24 | SQL inside Python | `pd.read_sql()`, and when to use SQL or pandas |

### Stage 5: JSON and open NHS APIs (planned)

| # | Topic | What I'll learn |
|---|-------|-----------------|
| 25 | JSON | How JSON maps to dictionaries and lists, `json.load()`, nested data |
| 26 | Calling an API | `requests.get()`, status codes and query parameters, using the ODS API to look up a GP practice |
| 27 | OpenPrescribing | Prescribing spending and measures data into a DataFrame |
| 28 | Fingertips | Public health indicators with `fingertips_py` (or its replacement, Find Public Health Data) |
| 29 | Being a good API user | Pagination, rate limits, caching results and handling errors |

### Stage 6: Health data standards and FHIR (planned)

| # | Topic | What I'll learn |
|---|-------|-----------------|
| 30 | Clinical codes | SNOMED CT, dm+d (VTM, VMP, AMP) and BNF codes, and how they map |
| 31 | Codes in analysis | Code lists, why searches miss patients, joining a code list to data |
| 32 | FHIR basics | Patient, Observation, MedicationRequest and Condition resources, and Bundles |
| 33 | A FHIR server | Searching a public FHIR test server with fictional patients |
| 34 | NHS FHIR | UK Core profiles, the NHS number and the ODS FHIR API |
| 35 | HL7 v2 and openEHR | Older message formats, integration engines and what openEHR adds |

### Stage 7: Population health methods (planned)

| # | Topic | What I'll learn |
|---|-------|-----------------|
| 36 | Rates and denominators | Rates per 1,000 and per 100,000, and small-number suppression |
| 37 | Confidence intervals | Wilson score intervals, and when a difference from England is real |
| 38 | Funnel plots | Control limits that show genuine outliers, not just small practices |
| 39 | Age standardisation | Directly standardised rates with the European Standard Population 2013 |
| 40 | Inequality gaps | IMD quintiles, the gap between most and least deprived, the slope index of inequality |
| 41 | Treatment gaps | Recorded versus expected prevalence, and the cost of closing a gap (actual and rebated) |

### Stage 8: Sharing results (planned)

| # | Topic | What I'll learn |
|---|-------|-----------------|
| 42 | Jupyter notebooks | Code, charts and written findings in one file |
| 43 | Charts that land | Titles that state the finding, and interactive charts with `plotly` |
| 44 | Automating a monthly report | Combining a folder of files, de-duplicating and writing formatted Excel |
| 45 | A simple dashboard | A web page with filters and charts using `streamlit` |
| 46 | Python in my everyday tools | Python in Excel and Power BI, where allowed |

### Capstone: a medicines inequalities report

Are antihypertensive prescribing and blood pressure control fair across deprivation? This project uses real open, aggregate data (OpenPrescribing, CVDPREVENT and deprivation scores) and brings every stage together: SQL storage, API data, code lists, confidence intervals, a funnel plot, the deprivation gap and a published notebook and dashboard.

### Git habits along the way

Commit after every lesson, add a `.gitignore` and `requirements.txt`, keep any API keys out of the repository, and work on a branch for each new lesson.

## Practice data

**No real patient data ever goes in this repository.** Lessons use fictional data, synthetic patients or open, aggregate NHS data only.

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

You need Python 3 installed. The book uses the Thonny editor on a Raspberry Pi, but any Python 3 setup works. Run the scripts from the top folder of the repository (not from inside `lessons/` or `answers/`), so they can find the `data` folder:

```bash
python lessons/4-variables.py
python answers/4-variables.py
```

Every lesson ends with a **Try it yourself** section of small exercises. My answers go in the matching file in [answers/](answers/).
