# ============================================================
# DAY 6 - Tuples in Python
#
# Topics Covered:
# 1. Creating Tuples
# 2. Accessing Elements
# 3. Tuple Slicing
# 4. Tuple Packing & Unpacking
# 5. Tuple Methods
# 6. Looping Through Tuples
# 7. Tuple Length
# 8. Difference Between List and Tuple
# ============================================================


# ============================================================
# CREATING TUPLES
# ============================================================

print("----- CREATING TUPLES -----")

fruits = ("apple", "banana", "mango", "orange")
numbers = (10, 20, 30, 40, 50)
mixed = ("Mansi", 19, 95.5, True)

print(fruits)
print(numbers)
print(mixed)


# ============================================================
# ACCESSING ELEMENTS
# ============================================================

print("\n----- ACCESSING ELEMENTS -----")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])


# ============================================================
# TUPLE SLICING
# ============================================================

print("\n----- TUPLE SLICING -----")

print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])
print(fruits[:])


# ============================================================
# TUPLES ARE IMMUTABLE
# ============================================================

print("\n----- TUPLES ARE IMMUTABLE -----")

print("Tuples cannot be changed after creation.")

# fruits[1] = "grapes"   # This will give an error


# ============================================================
# TUPLE PACKING & UNPACKING
# ============================================================

print("\n----- PACKING & UNPACKING -----")

# Packing
student = ("Mansi", 19, "Jalna")
print(student)

# Unpacking
name, age, city = student

print("Name:", name)
print("Age:", age)
print("City:", city)


# ============================================================
# TUPLE METHODS
# ============================================================

print("\n----- TUPLE METHODS -----")

nums = (10, 20, 30, 20, 40, 20)

print("Count of 20:", nums.count(20))
print("Index of 30:", nums.index(30))


# ============================================================
# LOOPING THROUGH TUPLES
# ============================================================

print("\n----- LOOPING THROUGH TUPLES -----")

for fruit in fruits:
    print(fruit)


# ============================================================
# TUPLE LENGTH
# ============================================================

print("\n----- TUPLE LENGTH -----")

print("Total fruits:", len(fruits))


# ============================================================
# MINI PRACTICE PROGRAMS
# ============================================================

print("\n----- MINI PRACTICE PROGRAMS -----")

# 1. Sum of tuple elements
data = (1, 2, 3, 4, 5)
print("Sum:", sum(data))


# 2. Find maximum and minimum
print("Maximum:", max(data))
print("Minimum:", min(data))


# 3. Check if an item exists
if "apple" in fruits:
    print("Apple is present")
else:
    print("Apple is not present")


# 4. Print even numbers
print("Even numbers:")
for n in data:
    if n % 2 == 0:
        print(n)


# ============================================================
# LIST vs TUPLE
# ============================================================

print("\n----- LIST vs TUPLE -----")

print("List  : Mutable (can be changed)")
print("Tuple : Immutable (cannot be changed)")


# ============================================================
# OUTPUT COMPLETE
# ============================================================

print("\nDay 6 completed successfully!")