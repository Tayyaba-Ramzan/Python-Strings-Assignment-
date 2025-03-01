# Python Strings Assignment 

# Part 1: Understanding String Literals 

# 1. Create three different strings using each type of quotation: 
# Single quotes ('example') 
# Double quotes ("example") 
# Triple quotes ("""example""") 

# Single quotes
string1 = 'This is a string using single quotes.'

# Double quotes
string2 = "This is a string using double quotes."

# Triple quotes
string3 = """This is a string using triple quotes."""

print(string1)
print(string2)
print(string3)

#                   XXXXXXXXXXXXXXXXXXXXX

# 2. Explain in your own words: What is the advantage of each type of quotation? 

# 1️⃣ Single Quotes (' ')
# Single quotes are best for short and simple strings. They keep the code concise and readable. However, if the string contains an apostrophe ('), you need to use an escape character (\).

# Example:
message = 'Hello, Python!'
# If the string contains an apostrophe:
message = 'It\'s a sunny day!'

# In this case, you need to escape the apostrophe (') using a backslash (\).

# 2️⃣ Double Quotes (" ")
# Double quotes are useful when the string contains a single quote ('). This avoids the need for an escape character, making the code cleaner and more readable.

# Example:
# message = "It's a beautiful day!"
# If the string contains double quotes:
# message = "He said, \"Python is amazing!\""
message = "He said, \"Python is amazing!\""
# Here, the escape character (\) is used to include double quotes inside the string.

# 3️⃣ Triple Quotes (""" """ or ''' ''')
# Triple quotes are ideal for multi-line strings, allowing you to write text across multiple lines without using escape characters. They are also commonly used for docstrings (documentation within functions).

# Multi-line string example:
message = """This is a 
multi-line string. 
It spans multiple lines."""
# Docstring example:

def greet():
    """This function prints a greeting message."""
    print("Hello, World!")
# This docstring describes the function and helps in documentation.

# If the string is short, using single (' ') or double (" ") quotes is a better choice. However, when writing multi-line text or documentation, triple quotes (""" """) are the best option!

#                   XXXXXXXXXXXXXXXXXXXXX

# 3. Write a string that contains both single and double quotes inside it. Example: She said, 
# "I'm going to the store." 

message = '''She said, "I'm going to the store."'''
print(message)

#                   XXXXXXXXXXXXXXXXXXXXX

# 4. Create a multi-line string using triple quotes that describes your favorite hobby. 

hobby_description = """My favorite hobby is coding.
I love solving challenging problems and building projects using Python and TypeScript.
Every day, I try to improve my skills by practicing algorithms, working on real-world applications,
and learning new programming concepts.

Coding is not just a skill for me; it's a passion that keeps me motivated and excited!"""
print(hobby_description)

#                   XXXXXXXXXXXXXXXXXXXXX