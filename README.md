# Python Data Structures

## Learning Outcomes assessed

- Data Structures
- Data Manipulation
- Recursion
- String Formatting

---

## Assessment Structure

The following Assessment has two sections:

- [Coding Assessment (Questions are below)](#fundamentals-coding-assessment)
- [Long Questions (Questions are below)](#long-format-questions) - `answers.txt`

You can answer them in any order.

---

## Your Goal

Read the instructions below for each [coding question](#fundamentals-coding-assessment), then complete each function in `data_structures.py` while ensuring that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass successfully

Read the instructions below for each [long format question](#long-format-questions), then add your answer under each relevant comment in `answers.txt` while ensuring that:

- You DO NOT remove the comments
- Read each question carefully before answering the question

---

### How to run your tests

To run all your tests

```bash
python3 -m pytest tests/test_data_structures.py -v
```

To run your tests individually

```bash
python3 -m pytest tests/test_data_structures.py::test_split_readings_logic -v
```

or for more information within the stacktrace use

```bash
python3 -m pytest tests/test_data_structures.py::test_split_readings_logic -vv
```

---

## Scoring & Weighting

| Component                                     | Weight  |
| --------------------------------------------- | ------- |
| Coding Section (unit tests)                   | **50%** |
| Long-format Question (answers.txt)            | **50%** |

## Fundamentals Coding Assessment

This assessment consists of seven Python functions. Each function has a partially written
implementation. Your task is to **fix the bugs**, **complete the missing logic**, and **ensure all tests pass**.

### Project Structure

```text
fun-003-data-structures/
├── data_structures.py              # <-- This is where you write your solutions
├── answers.txt                     # <-- This is where you write your answers to the long questions
├── tests/
│   └── test_data_structures.py     # <-- These are the tests you must make pass
└── README.md                       # <-- Assessment instructions (this file) 
```

---

### Question 1 - `split_readings(readings)`

The South African Astronomical Observatory near *Sutherland* in the Northern Cape sits in one of the coldest, clearest corners of the country, which is why the Southern African Large Telescope was built there. A weather station on the site records the temperature once an hour, storing every reading as a pair of $(hour, temperature)$ values. The astronomers need these readings separated: one list containing only the *hours* (the time axis for their chart) and another containing only the *temperatures* (the value axis).

Apply your logic to the `split_readings()` function. You will receive a list of tuples, where each tuple contains two numbers. Your goal is to \"unzip\" or split these pairs into two separate lists.

- **Input:**

```python
[(6, 4), (12, 18), (18, 11)]
```

- **Output:**

```python
([6, 12, 18], [4, 18, 11])
```

Constraint: A tuple that does not contain exactly two values, or an element that is not a tuple at all, must not be silently ignored.

---

### Question 2 - `create_seat_lookup(passengers)`

It is the Friday afternoon rush at *Park Station* in Johannesburg and the Gautrain to Pretoria is filling up. The conductors have a list of passenger names in the order they boarded, and each passenger is given the seat number matching their position in that list (the first passenger gets seat `0`, the second seat `1`, and so on).

To help passengers who forget where they are sitting, the conductors want a quick lookup: type in a name and immediately get back the seat number.

Apply your logic to the `create_seat_lookup()` function. The function takes a list of names and should return a dictionary where each passenger's name is the key and their seat number (index) is the value. If the same name appears more than once, the dictionary keeps the **latest** position.

- **Input:**

```python
["Naledi", "Pieter", "Zodwa", "Anele"]
```

- **Output:**

```python
{"Naledi": 0, "Pieter": 1, "Zodwa": 2, "Anele": 3}
```

---

### Question 3 - `extract_unique_hashtags(posts)`

You are the data analyst for the *Cape Town International Jazz Festival*. The social media team collects hundreds of thousands of posts every weekend, and the hashtags they capture are messy: some are typed in capitals, some have accidental spaces at the start or end, and some are completely blank because of a scraping error. Before the team can count how many different topics fans are talking about, the tags must be cleaned.

Apply your logic to the `extract_unique_hashtags()` function. You must transform the list of raw tags into a set of unique, lowercase strings with surrounding whitespace removed. Blank entries (empty strings or strings containing only whitespace) must be ignored.

- **Input:**

```python
['  Amapiano', 'amapiano ', 'JAZZ', 'Jazz', 'Braai', ' braai', '']
```

- **Output:**

```python
{'amapiano', 'jazz', 'braai'}
```

---

### Question 4 - `group_by_genre(books)`

The *Johannesburg Central Library* has received a trolley of returned books, and the librarians need them shelved by genre so the returns can be packed away without walking back and forth between sections.

Apply your logic to the `group_by_genre()` function. You will take a list of dictionaries, each containing a `title` and a `genre`, and transform them into a single dictionary where each `genre` is a key, and its value is a list of all book `titles` belonging to that genre, in the order they appeared.

- **Input:**

```python
[{"title": "Cry, the Beloved Country", "genre": "Fiction"}, {"title": "Long Walk to Freedom", "genre": "Biography"}, {"title": "Spud", "genre": "Fiction"}, {"title": "Born a Crime", "genre": "Biography"}]
```

- **Output:**

```python
{"Fiction": ["Cry, the Beloved Country", "Spud"], "Biography": ["Long Walk to Freedom", "Born a Crime"]}
```

---

### Question 5 - `batch_parcel_dispatcher(parcel_ids)`

A courier company in *Bloemfontein* delivers parcels around the city using small vans. Each van can only carry a maximum of 4 parcels per trip, otherwise the doors will not close and the van becomes unsafe to drive.

You have a list (or tuple) of `parcel_ids` that need to be delivered. Your job is to help the dispatcher organise these IDs into smaller groups (sublists) so that each van trip is within its limit.

Apply your logic to the `batch_parcel_dispatcher()` function. The function should take the full collection of IDs and break them down into a nested list where each internal "trip" contains a maximum of 4 IDs. If the total number of parcels is not a perfect multiple of 4, the final trip will simply contain the remaining IDs. Every trip must be a `list`, even when the input is a tuple, and the original input must not be changed.

- **Input:**

```python
['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']
```

- **Output:**

```python
[['P1', 'P2', 'P3', 'P4'], ['P5', 'P6', 'P7', 'P8'], ['P9']]
```

Constraint: No sublist should ever exceed 4 items.

---

### Question 6 - `taxi_rank_inverter(driver_routes)`

Minibus taxis are the backbone of public transport in Johannesburg. The association keeps records based on each driver: which taxi ranks does this driver serve (e.g. "Themba serves Bree and Noord").

However, the rank marshals need the opposite: for every rank, which drivers can be expected to arrive there? 

Apply your solution to the `taxi_rank_inverter()` function. You are given a dictionary where the keys are drivers and the values are lists of ranks they serve. You must return a new dictionary where the keys are the ranks and the values are lists of the drivers who serve them. A driver must only appear once per rank, even if the same rank is listed twice on their route, and the drivers must appear in the order they were found. The original dictionary must not be changed, and the lists in the result must be new lists.

- **Input:**

```python
{"Themba": ["Bree", "Noord"], "Zanele": ["Noord"]}
```

- **Output:**

```python
{"Bree": ["Themba"], "Noord": ["Themba", "Zanele"]}
```

*Clarity: Because Themba serves Bree, Bree now has Themba in its list of drivers. Because both Themba and Zanele serve Noord, Noord has both of them in its list.*

---

### Question 7 - `factorial_sequence(n)`

Rangers in the *Kruger National Park* plan their patrols around waterholes. If a ranger must visit $k$ different waterholes, the number of different orders in which the visits can be made is $k!$ (k factorial: $k \times (k-1) \times \dots \times 1$, with $0! = 1$). The park manager wants to see how quickly the number of possible patrol routes grows as more waterholes are added, so she needs the list of these values for $0$ up to $n-1$ waterholes.

Apply your solution to the `factorial_sequence(n)` function. The function should take an integer $n$ and return a list containing the first $n$ factorial numbers, starting from $0!$.

Your solution **must use recursion**. A negative number or a value that is not an integer must raise a `ValueError`.

- **Input:**

```python
n = 6
```

- **Output:**

```python
[1, 1, 2, 6, 24, 120]
```

---

## Long-Format Questions

Please answer these in the `answers.txt` file (**DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT**)

### Question 1

Explain what it means for a Python object to be hashable, and why a tuple can be used as a dictionary key but a list cannot. Give one example of each, and explain one practical situation where using a tuple as a dictionary key would be useful.

### Question 2

A program must check whether a learner number has already been registered among hundreds of thousands of existing records. Compare using a list, a set and a dictionary to do this check, explaining how each stores its data and how that affects the speed of the lookup as the amount of data grows.

### Question 3

You are building a print queue for a school computer lab. Print jobs are added to the end of the queue as learners submit them, and are processed from the front of the queue, one at a time, in the order they arrived. The same document may be submitted more than once. Explain what characteristics the data structure managing the queue must have, and why certain data structures are more appropriate than others for this task.

---

Good luck — and remember to think carefully about your solutions!