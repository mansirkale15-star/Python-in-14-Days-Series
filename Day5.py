# ============================================================
# DAY 5 - LISTS
#
# Topics Covered:
# 1. Creating Lists
# 2. Accessing Elements
# 3. List Slicing
# 4. Updating Lists
# 5. Adding Elements
# 6. Removing Elements
# 7. List Methods
# 8. Looping Through Lists
# 9. Nested Lists
# 10. List Comprehension
# ============================================================


# ============================================================
# CREATING LISTS
# ============================================================

print("----- CREATING LISTS -----")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)
print(type(fruits))


# ============================================================
# ACCESSING ELEMENTS
# ============================================================

print("\n----- ACCESSING ELEMENTS -----")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])


# ============================================================
# LIST SLICING
# ============================================================

print("\n----- LIST SLICING -----")

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[-3:])
print(numbers[::-1])


# ============================================================
# UPDATING LISTS
# ============================================================

print("\n----- UPDATING LISTS -----")

colors = ["Red", "Green", "Blue"]

print("Before:", colors)

colors[1] = "Yellow"

print("After:", colors)


# ============================================================
# ADDING ELEMENTS
# ============================================================

print("\n----- ADDING ELEMENTS -----")

students = ["Raj", "Mansi", "Amit"]

students.append("Priya")
print("After append():", students)

students.insert(1, "Rahul")
print("After insert():", students)

students.extend(["Sneha", "Rohan"])
print("After extend():", students)


# ============================================================
# REMOVING ELEMENTS
# ============================================================

print("\n----- REMOVING ELEMENTS -----")

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)
print("After remove():", numbers)

numbers.pop()
print("After pop():", numbers)

numbers.pop(1)
print("After pop(index):", numbers)

del numbers[0]
print("After del:", numbers)


# ============================================================
# LIST METHODS
# ============================================================

print("\n----- LIST METHODS -----")

marks = [85, 92, 78, 60, 92, 88]

print("Length:", len(marks))
print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Sum:", sum(marks))

print("Count of 92:", marks.count(92))
print("Index of 78:", marks.index(78))

marks.sort()
print("Ascending:", marks)

marks.sort(reverse=True)
print("Descending:", marks)

marks.reverse()
print("Reverse:", marks)

copy_marks = marks.copy()
print("Copied List:", copy_marks)


# ============================================================
# LOOPING THROUGH LISTS
# ============================================================

print("\n----- LOOPING THROUGH LISTS -----")

subjects = ["Python", "SQL", "Machine Learning", "Power BI"]

for subject in subjects:
    print(subject)


print("\nUsing Index")

for i in range(len(subjects)):
    print(i, "-", subjects[i])


# ============================================================
# NESTED LISTS
# ============================================================

print("\n----- NESTED LISTS -----")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(matrix[0])
print(matrix[1][2])
print(matrix[2][1])


# ============================================================
# LIST COMPREHENSION
# ============================================================

print("\n----- LIST COMPREHENSION -----")

numbers = [1, 2, 3, 4, 5]

square = [num ** 2 for num in numbers]

print(square)

even = [num for num in numbers if num % 2 == 0]

print(even)


# ============================================================
# MINI PROJECT 1
# Student Marks Manager
# ============================================================

print("\n===== STUDENT MARKS MANAGER =====")

marks = []

n = int(input("How many marks do you want to enter? "))

for i in range(n):
    mark = int(input(f"Enter Mark {i+1}: "))
    marks.append(mark)

print("\nMarks:", marks)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks)/len(marks))


# ============================================================
# MINI PROJECT 2
# Shopping Cart
# ============================================================

print("\n===== SHOPPING CART =====")

cart = []

while True:

    item = input("Enter item (or type 'done'): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("\nItems in Cart:")

for item in cart:
    print("-", item)

print("Total Items:", len(cart))


# ============================================================
# MINI PROJECT 3
# Largest Number Finder
# ============================================================

print("\n===== LARGEST NUMBER FINDER =====")

numbers = []

size = int(input("How many numbers? "))

for i in range(size):
    num = int(input("Enter Number: "))
    numbers.append(num)

print("Numbers:", numbers)
print("Largest Number:", max(numbers))


# ============================================================
# MINI PROJECT 4
# Remove Duplicate Elements
# ============================================================

print("\n===== REMOVE DUPLICATES =====")

numbers = [10, 20, 30, 20, 10, 40, 50, 40]

print("Original List:", numbers)

unique = []

for item in numbers:

    if item not in unique:
        unique.append(item)

print("Without Duplicates:", unique)


# ============================================================
# MINI PROJECT 5
# To-Do List Manager
# ============================================================

print("\n===== TO-DO LIST MANAGER =====")

tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        task = input("Enter Task: ")
        tasks.append(task)

    elif choice == "2":

        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No Tasks Available")

        else:

            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")