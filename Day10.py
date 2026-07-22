# ============================================================
# DAY 10 - File Handling in Python
#
# Topics Covered:
# 1. Creating Files
# 2. File Modes
# 3. Writing to a File
# 4. Reading from a File
# 5. Appending Data
# 6. with open()
# 7. readline() & readlines()
# 8. File Pointer (tell & seek)
# 9. Working with CSV Files
# 10. Mini Project
# ============================================================

import csv

# ============================================================
# WRITING TO A FILE
# ============================================================

print("----- WRITING TO A FILE -----")

file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This is Day 10 of Python Series.\n")

file.close()

print("Data Written Successfully.")


# ============================================================
# READING A FILE
# ============================================================

print("\n----- READING FILE -----")

file = open("sample.txt", "r")

print(file.read())

file.close()


# ============================================================
# APPENDING DATA
# ============================================================

print("\n----- APPENDING DATA -----")

file = open("sample.txt", "a")

file.write("Appending a new line.\n")

file.close()

print("Data Appended Successfully.")


# ============================================================
# USING with open()
# ============================================================

print("\n----- WITH OPEN -----")

with open("sample.txt", "r") as file:
    print(file.read())


# ============================================================
# READLINE
# ============================================================

print("\n----- READLINE -----")

with open("sample.txt", "r") as file:
    print(file.readline())
    print(file.readline())


# ============================================================
# READLINES
# ============================================================

print("\n----- READLINES -----")

with open("sample.txt", "r") as file:
    lines = file.readlines()

print(lines)


# ============================================================
# FILE POINTER
# ============================================================

print("\n----- FILE POINTER -----")

with open("sample.txt", "r") as file:

    print(file.read(10))

    print("Pointer Position:", file.tell())

    file.seek(0)

    print(file.read(10))


# ============================================================
# CSV FILE WRITING
# ============================================================

print("\n----- CSV WRITING -----")

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])

    writer.writerow([101, "Mansi", 95])

    writer.writerow([102, "Rahul", 89])

print("CSV Created Successfully.")


# ============================================================
# CSV FILE READING
# ============================================================

print("\n----- CSV READING -----")

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# PRACTICE PROGRAM 1
# ============================================================

print("\n----- PRACTICE 1 -----")

text = input("Enter a sentence: ")

with open("practice.txt", "w") as file:
    file.write(text)

print("Saved Successfully.")


# ============================================================
# PRACTICE PROGRAM 2
# ============================================================

print("\n----- PRACTICE 2 -----")

with open("practice.txt", "r") as file:
    print(file.read())


# ============================================================
# MINI PROJECT
# ============================================================

print("\n========== STUDENT RECORD ==========")

name = input("Enter Student Name: ")
marks = input("Enter Marks: ")

with open("records.txt", "a") as file:
    file.write(name + "," + marks + "\n")

print("Record Saved Successfully.")

print("\n----- ALL RECORDS -----")

with open("records.txt", "r") as file:
    print(file.read())


# ============================================================
# DAY 10 COMPLETED
# ============================================================

print("\n🎉 Congratulations!")
print("You have completed Day 10 - File Handling.")