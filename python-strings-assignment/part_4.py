# Python Strings Assignment 

# Part 4: Combining String Methods with F-Strings 

# Create a program that: 
# 1. Asks for user input about their first name, last name, and birth year 
# 2. Uses string methods to properly capitalize their name 
# 3. Uses f-strings to create a profile message: "Profile: {First Last}, Age: {calculated age}, 
# Username: {first initial + last name + birth year}" 

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
birth_year = input("Enter your birth year: ").strip()

first_name = first_name.capitalize()
last_name = last_name.capitalize()

current_year = 2024 
age = current_year - int(birth_year)

username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"

print(f"Profile: {first_name} {last_name}, Age: {age}, Username: {username}")
