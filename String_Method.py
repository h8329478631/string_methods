
str1 = "i love python programming"

print("string = ",str1)

# 1. upper method
upper_method = str1.upper()
print("1. upper method = ",upper_method)

# 2. lower method
lower_method = str1.lower()
print("2. lower method = ",lower_method)

# 3. capitalize method
capitalize_method = str1.capitalize()
print("3. capitalize method = ",capitalize_method)

# 4. casefold method
casefold_method = str1.casefold()
print("4. casefold method = ",casefold_method)

# 5. find method - find = pro
find_method = str1.find("r")
print("5. find method (str1.find(""\"r""\") = ",find_method)

# 6. sorted method -
sorted_method = sorted(str1)
print("6. sorted method = ",sorted_method)

# 7. sorted method - reverse
sorted_reverse_method = sorted(str1,reverse=True)
print("7. sorted method = ",sorted_reverse_method)

# 8. replace method - 
replace_method = str1.replace("programming","code")
print("8. replace method (programming to code) = ",replace_method)

# 9. split method - 
split_method = str1.split() #When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard
print("8. split method  = ",split_method)

# 10. index method -
index_method = str1.index("p")
print("10. index method = ",index_method)

# 11. removesuffix method - this method help to removing last occurence char/word
removesuffix_method = str1.removesuffix("programming")
print("11. removesuffix_method = ",removesuffix_method) 

# 12. removeprefix method - this method help to removing first occurence char/word
removeprefix_method = str1.removeprefix("i love")
print("11. removeprefix_method = ",removeprefix_method)  