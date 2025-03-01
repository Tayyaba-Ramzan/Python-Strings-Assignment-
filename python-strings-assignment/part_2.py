# Python Strings Assignment 

# Part 2: String Methods Practice 

# 1. Create a variable full_name with your full name (first and last name). Then write code 
# to: 
# Print your name in all uppercase letters 
# Print your name in all lowercase letters 
# Print your name with the first letter of each name capitalized 

first_name="Tayyaba"
last_name="Ramzan"
full_name=first_name + " " + last_name
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())

#                   XXXXXXXXXXXXXXXXXXXXX

# 2. Create a variable messy_text = " Python programming is fun! " Then write code 
# to: 
# Remove all the extra spaces at the beginning and end 
# Replace "fun" with "amazing" 
# Count how many times the letter 'i' appears 

messy_text = " Python programming is fun! "
print(messy_text.strip())
print(messy_text.replace("fun","amazing"))
print(messy_text.count("i"))

#                   XXXXXXXXXXXXXXXXXXXXX

# 3. Create a variable sentence = "The quick brown fox jumps over the lazy dog" 
# Then write code to: 
# Split this sentence into a list of words 
# Join the words back together with dashes between them 
# Check if the sentence starts with "The" 
# Find the position of the word "fox" 

sentence = "The quick brown fox jumps over the lazy dog"

words_list = sentence.split(" ")
print(words_list)

joined_sentence = "-".join(words_list)
print(joined_sentence)

sentence = "The quick brown fox jumps over the lazy dog"
starts_with_the = sentence.startswith("The")
print(starts_with_the)  

fox_position = sentence.find("fox")
print(fox_position) 

#                   XXXXXXXXXXXXXXXXXXXXX



