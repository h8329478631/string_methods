🐍 Python String Methods Practice

This project contains basic Python string method examples for learning and practice.

📌 Topics Covered

Case Conversion Methods

Whitespace Removal

Split & Join

Searching & Finding

Replace Method

Boolean String Checks

Partitioning

Formatting (Old & f-String)

Sorting Strings

Length Calculation

Special String Methods

🔤 1️⃣ Case Conversion Methods
Method	Description	Example
upper()	Converts to uppercase	"hello".upper() → HELLO
lower()	Converts to lowercase	"HELLO".lower() → hello
capitalize()	Capitalizes first letter	"hello world" → Hello world
title()	Converts to title case	"hello world" → Hello World
casefold()	Strong lowercase (used for comparisons)	"PYTHON" → python
✂️ 2️⃣ Removing Spaces
Method	Description
strip()	Removes leading & trailing spaces
lstrip()	Removes leading spaces
rstrip()	Removes trailing spaces
🔍 3️⃣ Searching & Finding
Method	Description
find()	Finds first occurrence (returns -1 if not found)
rfind()	Finds last occurrence
index()	Finds index (gives error if not found)
count()	Counts occurrences
🔁 4️⃣ Replace Method
"I love Java".replace("Java", "Python")


✔ Output: I love Python

🔗 5️⃣ Split & Join
"apple banana grape".split()


✔ Output: ['apple', 'banana', 'grape']

" ".join(['Python', 'is', 'fun'])


✔ Output: Python is fun

🔎 6️⃣ Checking Methods
Method	Checks
isalpha()	Only alphabets
isdigit()	Only digits
isalnum()	Alphabets + digits
isspace()	Only spaces
isnumeric()	Numeric characters
isupper()	All uppercase
islower()	All lowercase
istitle()	Title case
isidentifier()	Valid Python variable name
isprintable()	Printable characters
📂 7️⃣ Partitioning
"python-programming-language".partition("-")


✔ Output: ('python', '-', 'programming-language')

"one-two-three".rpartition("-")


✔ Splits from right side

🔢 8️⃣ Formatting Strings
Old Method
"Hey my name is {0}".format("Harshal")

f-String (Recommended)
name = "Harshal"
print(f"My name is {name}")

Float Formatting
price = 49.5263
print(f"{price:.2f}")


✔ Output: 49.53

➕ 9️⃣ Other Useful Examples

zfill(5) → Pads with zeros

len(string) → Finds length

sorted(string) → Sort characters

sorted(string, reverse=True) → Descending order

bool(0) → False

List addition → [1,2] + [3,4]

📚 Learning Purpose

This file covers beginner-level Python string methods useful for:

Interviews

Company assessments

Practice exercises

Daily coding tasks

👨‍💻 Author

Harshu 
Python Learner 🚀