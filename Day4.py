# ============================================================
# DAY 4 - Strings
#
# Topics Covered:
# 1. Creating Strings
# 2. Indexing
# 3. Slicing
# 4. String Operators
# 5. String Methods
# 6. Escape Characters
# 7. f-Strings
# ============================================================


# ============================================================
# CREATING STRINGS
# ============================================================

print("----- CREATING STRINGS -----")

name = "Mansi"

print(name)
print(type(name))


# ============================================================
# INDEXING
# ============================================================

print("\n----- INDEXING -----")

text = "Python"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])


# ============================================================
# SLICING
# ============================================================

print("\n----- SLICING -----")

language = "Python Programming"

print(language[0:6])
print(language[7:])
print(language[:6])
print(language[-11:])
print(language[::-1])


# ============================================================
# STRING OPERATORS
# ============================================================

print("\n----- STRING OPERATORS -----")

first = "Hello"
second = "World"

print(first + " " + second)
print(first * 3)


# ============================================================
# STRING METHODS
# ============================================================

print("\n----- STRING METHODS -----")

sentence = "python programming"

print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())

print(sentence.replace("python", "Java"))

print(sentence.count("m"))

print(sentence.find("program"))

print(sentence.startswith("python"))

print(sentence.endswith("ing"))


# ============================================================
# STRIP
# ============================================================

text = "   Python   "

print(text.strip())


# ============================================================
# SPLIT & JOIN
# ============================================================

skills = "Python SQL Excel"

print(skills.split())

languages = ["Python", "SQL", "Power BI"]

print(" | ".join(languages))


# ============================================================
# ESCAPE CHARACTERS
# ============================================================

print("\n----- ESCAPE CHARACTERS -----")

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python is Awesome\"")


# ============================================================
# F-STRINGS
# ============================================================

print("\n----- F-STRINGS -----")

name = "Mansi"
age = 22

print(f"My name is {name} and I am {age} years old.")

# ---------------- Password Strength Checker ----------------

password = input("Create a password: ")

if len(password) >= 8:

    if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):

        print("Strong Password")

    else:
        print("Password should contain both letters and numbers.")

else:
    print("Password should be at least 8 characters long.")


# ---------------- Word Counter ----------------

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Total Words:", len(words))


# ---------------- Palindrome Checker ----------------

text = input("Enter a word: ")

if text.lower() == text[::-1].lower():
    print("Palindrome")
else:
    print("Not a Palindrome")

#---------------- Vowel Counter ----------------    

vowels = "aeiou"

text = input("Enter a sentence: ").lower()

count = 0

for letter in text:

    if letter in vowels:
        count += 1

print("Total Vowels:", count)
