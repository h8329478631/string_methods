#1. Write a Python program to convert the given string "hello world" to uppercase.

q1 = "hello world"

print(q1.upper())

#2. Convert the string "Python Programming" to lowercase.

q2 = "Python Programming"

print(q2.lower())

#3. Capitalize the first letter of "hello python learners".

q3 = "hello python learners"

print(q3.capitalize())

#4. Convert "welcome to python" to title case.

q4 = "welcome to python"

print(q4.title())

#	5. Remove leading and trailing spaces from the string " Python String Functions " using strip().

q5 = "  Python String Functions"
print(q5)
print(q5.strip())

#	6. Remove only trailing spaces from "Hello World " .

q6 = "Hello World "
print(q6,"end")
print(q6.rstrip(),"end")

#	7. Remove only leading spaces from " Learn Python".

q7 = " Learn Python"
print(q7)
print(q7.lstrip())

#	8. Split the string "apple banana grape" into a list using split().

q8 = "apple banana grape"
splt  = q8.split()
print(splt)

#	9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.

q9 = ['Python', 'is', 'fun']
jnd = " ".join(q9)
print(jnd)

#  10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().

q10 = ['A', 'B', 'C']
join_list = "-".join(q10)

print(join_list)

# 11. Find the index of the first occurrence of "Python" in "I love Python programming".

q11 = "I love Python programming"

print(q11.find("Python"))

# 12. Find the last occurrence of "o" in "Hello World".

q12 = "Hello World"
print(q12.find("o",5))

#  13. Replace "Java" with "Python" in the string "I love Java".

q13 = "I love Java"
print(q13.replace("Java","Python"))

# 14. Check if the string "Hello World" starts with "Hello".

q14 = "Hello World"

print(q14.startswith("Hello"))

# 15. Check if the string "example.txt" ends with ".txt".

q15 = "example.txt"

print(q15.endswith(".txt"))

#  16. Count the occurrences of "o" in "Hello, how are you?".

q16 = "Hello, how are you?"

print(q16.count("o"))

# 17. Find the index of "r" in "programming".

q17 = "programming"

print(q17.index("r"))

# 18. Try finding the index of "z" in "python" using index(), and observe the error.

# q18 = "python"

# print(q18.index("z"))

#  19. find the last occurrence of "e" in "experience".

q19 = "experience"

print(q19.rfind("e"))

#  20. find the first occurrence of "e" in "experience".

q20 = "experience"

print(q20.find("e"))

# 21. Check if the string "Python" contains only alphabets.

q21 = "Python"
print(q21.isalpha())

# 22. Verify if "12345" contains only digits.

q22 = "12345"

print(q22.isdigit())

#  23. Check if "Python123" is alphanumeric.

q23 = "Python123"

print(q23.isalnum())

# 24. Test if the string " " consists of only spaces.

q24 = " "

print(q24.isspace())

# 25. Check if "12345" is numeric using.

q25 = "12345" 

print(q25.isnumeric())

# 27. Partition the string "python-programming-language" at "-".

q27 = "python-programming-language"

print(q27.partition("-"))


#28. Use rpartition() to split "one-two-three" from the right sing "-".

q28 = "python-programming-language"

print(q28.rpartition("-"))

#  29. Convert "PYTHON" to lowercase using casefold().

q29 = "PYTHON"

print(q29.casefold())

# 30. Convert "42" into a 5-character string padded with zeros using zfill().

q30 = "42"

print(q30.zfill(5))

# 31. Check if "HELLO" is in uppercase.

q31 = "HELLO"

print(q31.isupper())

#  32. Verify if "hello" is in lowercase.

q32 = "hello"

print(q32.islower())

# 33. Check if "Python Programming" follows title case.

q33 = "Python Programming"

print(q33.istitle())


# 34. Sort the characters of "banana" alphabetically.

q34 = "banana"

print(sorted(q34))

# 35. Find the length of the string "Data Science".

q35 = "Data Science"

print(len(q35))

# 36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.
q36 = "The Kiran  Academy"

print(sorted(q36,reverse=True))


# printable method

q37 = "hello \t world"

q38 = "hello /t world"

if q37.isprintable():
    print("q37 is right",q37)
elif q38.isprintable():
    print("q38 is right",q38)
else:
    print("something went wrong")


print("1num".isidentifier())
print("_num".isidentifier())



#  26. Use format() to insert "Python" and "fun" into the string "{} is {}!".

#old method

letter = "hey my name is {0} and i am from {1}"

name = "Harshal"
country = "India"

print(letter.format(name,country))

#and new implemented method

print(f"hey my name is {name} and i am from {country}")

price = 49.5263

print(f"{price:.2f}")

#if you want to calculate some num and get in str datatype so try this following method

calc = f"{2*3}"

print(calc)
print(type(calc))


#if you want to print f string curly braces as it is so use following method

print(f"hello my name is {{name}}")

print([1,2]+[3,4])
print(bool(0))

q30.toupper