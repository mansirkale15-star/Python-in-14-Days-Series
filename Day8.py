# ============================================================
# DAY 8 - Dictionaries
#
# Topics Covered:
# 1. Creating Dictionaries
# 2. Accessing Values
# 3. Updating Values
# 4. Adding New Items
# 5. Removing Items
# 6. Dictionary Methods
# 7. Looping Through Dictionary
# 8. Nested Dictionary
# ============================================================


# ============================================================
# CREATING DICTIONARIES
# ============================================================

print("----- CREATING DICTIONARIES -----")

student = {
    "name": "Mansi",
    "age": 19,
    "course": "Data Science"
}

print(student)


# ============================================================
# ACCESSING VALUES
# ============================================================

print("\n----- ACCESSING VALUES -----")

print(student["name"])
print(student["age"])

# Using get()
print(student.get("course"))

# If key doesn't exist
print(student.get("city"))        # None
print(student.get("city", "Not Found"))


# ============================================================
# UPDATING VALUES
# ============================================================

print("\n----- UPDATING VALUES -----")

student["age"] = 20
print(student)


# ============================================================
# ADDING NEW ITEMS
# ============================================================

print("\n----- ADDING NEW ITEMS -----")

student["city"] = "Jalna"
student["college"] = "Badrinarayan Barwale College"

print(student)


# ============================================================
# REMOVING ITEMS
# ============================================================

print("\n----- REMOVING ITEMS -----")

student.pop("city")
print(student)

del student["college"]
print(student)


# ============================================================
# DICTIONARY METHODS
# ============================================================

print("\n----- DICTIONARY METHODS -----")

print(student.keys())
print(student.values())
print(student.items())


# ============================================================
# LOOPING THROUGH DICTIONARY
# ============================================================

print("\n----- LOOPING THROUGH KEYS -----")

for key in student:
    print(key)

print("\n----- LOOPING THROUGH VALUES -----")

for value in student.values():
    print(value)

print("\n----- LOOPING THROUGH KEY & VALUE -----")

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# NESTED DICTIONARY
# ============================================================

print("\n----- NESTED DICTIONARY -----")

students = {
    101: {
        "name": "Rahul",
        "Marks": 90
    },
    102: {
        "name": "Mansi",
        "Marks": 95
    }
}

print(students)

print(students[101]["name"])
print(students[102]["Marks"])


# ============================================================
# PRACTICE EXAMPLES
# ============================================================

print("\n----- PRACTICE 1 -----")

car = {
    "Brand": "BMW",
    "Model": "X5",
    "Year": 2024
}

print(car)

print("\n----- PRACTICE 2 -----")

employee = {}

employee["Name"] = "Raj"
employee["Salary"] = 50000
employee["Department"] = "IT"

print(employee)

print("\n----- PRACTICE 3 -----")

marks = {
    "Math": 90,
    "Science": 88,
    "English": 95
}

total = sum(marks.values())

print("Total Marks :", total)
print("Average :", total / len(marks))


# ============================================================
# MINI PROJECT
# ============================================================

print("\n========== STUDENT RECORD ==========")

student = {}

student["Name"] = input("Enter Name : ")
student["Age"] = int(input("Enter Age : "))
student["Course"] = input("Enter Course : ")
student["Marks"] = float(input("Enter Marks : "))

print("\n----- STUDENT DETAILS -----")

for key, value in student.items():
    print(f"{key} : {value}")


# ============================================================
# DAY 8 COMPLETED
# ============================================================

print("\n🎉 Congratulations!")
print("We have completed Day 8 - Dictionaries.")