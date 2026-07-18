# ============================================================
# DAY 7 - Sets in Python
#
# Topics Covered:
# 1. Creating Sets
# 2. Accessing Elements
# 3. Adding Elements
# 4. Removing Elements
# 5. Set Operations
# 6. Looping Through Sets
# 7. Set Length
# 8. Difference Between List, Tuple and Set
# ============================================================


# ============================================================
# CREATING SETS
# ============================================================

print("----- CREATING SETS -----")

fruits = {"apple", "banana", "mango", "orange"}
numbers = {10, 20, 30, 40, 50}

print(fruits)
print(numbers)


# ============================================================
# DUPLICATES ARE NOT ALLOWED
# ============================================================

print("\n----- DUPLICATES -----")

data = {1, 2, 3, 3, 4, 4, 5}
print(data)


# ============================================================
# ACCESSING ELEMENTS
# ============================================================

print("\n----- ACCESSING ELEMENTS -----")

print("Sets do not support indexing.")

for item in fruits:
    print(item)


# ============================================================
# ADDING ELEMENTS
# ============================================================

print("\n----- ADDING ELEMENTS -----")

fruits.add("pineapple")
print(fruits)

fruits.update(["kiwi", "grapes"])
print(fruits)


# ============================================================
# REMOVING ELEMENTS
# ============================================================

print("\n----- REMOVING ELEMENTS -----")

fruits.remove("banana")
print(fruits)

fruits.discard("orange")
print(fruits)

removed = fruits.pop()
print("Removed:", removed)
print(fruits)


# ============================================================
# SET OPERATIONS
# ============================================================

print("\n----- SET OPERATIONS -----")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)


# ============================================================
# LOOPING THROUGH SETS
# ============================================================

print("\n----- LOOPING THROUGH SETS -----")

for item in A:
    print(item)


# ============================================================
# SET LENGTH
# ============================================================

print("\n----- SET LENGTH -----")

print("Length of A:", len(A))


# ============================================================
# MEMBERSHIP TESTING
# ============================================================

print("\n----- MEMBERSHIP TESTING -----")

if 3 in A:
    print("3 is present in A")
else:
    print("3 is not present in A")


# ============================================================
# MINI PRACTICE PROGRAMS
# ============================================================

print("\n----- MINI PRACTICE PROGRAMS -----")

# 1. Remove duplicates from a list
list_data = [1, 2, 2, 3, 3, 4, 5, 5]
unique = set(list_data)
print("Unique values:", unique)


# 2. Common values between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)
print("Common values:", common)


# 3. Unique values from both lists
all_unique = set(list1) | set(list2)
print("All unique values:", all_unique)


# ============================================================
# LIST vs TUPLE vs SET
# ============================================================

print("\n----- LIST vs TUPLE vs SET -----")

print("List  : Ordered, Mutable, Allows Duplicates")
print("Tuple : Ordered, Immutable, Allows Duplicates")
print("Set   : Unordered, Mutable, No Duplicates")


# ============================================================
# OUTPUT COMPLETE
# ============================================================

print("\nDay 7 completed successfully!")