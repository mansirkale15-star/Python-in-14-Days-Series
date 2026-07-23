# ============================================================
# DAY 11 - Exception Handling in Python
#
# Topics Covered:
# 1. What is an Exception?
# 2. try and except
# 3. Handling Specific Exceptions
# 4. Multiple Exceptions
# 5. else Block
# 6. finally Block
# 7. raise Keyword
# 8. Custom Exception
# 9. Mini Project - Safe Calculator
# ============================================================


# ============================================================
# SIMPLE EXCEPTION
# ============================================================

print("----- SIMPLE EXCEPTION -----")

try:
    num = 10 / 0
    print(num)

except:
    print("An error occurred.")


# ============================================================
# SPECIFIC EXCEPTION
# ============================================================

print("\n----- SPECIFIC EXCEPTION -----")

try:
    number = int(input("Enter a Number: "))
    print(number)

except ValueError:
    print("Please enter only numbers.")


# ============================================================
# MULTIPLE EXCEPT BLOCKS
# ============================================================

print("\n----- MULTIPLE EXCEPT -----")

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")


# ============================================================
# ELSE BLOCK
# ============================================================

print("\n----- ELSE BLOCK -----")

try:
    x = 20
    y = 5

    print(x / y)

except ZeroDivisionError:
    print("Error")

else:
    print("Division Successful")


# ============================================================
# FINALLY BLOCK
# ============================================================

print("\n----- FINALLY BLOCK -----")

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Execution Finished.")


# ============================================================
# RAISE KEYWORD
# ============================================================

print("\n----- RAISE KEYWORD -----")

age = int(input("Enter Your Age: "))

try:

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible")

except ValueError as e:
    print(e)


# ============================================================
# CUSTOM EXCEPTION
# ============================================================

print("\n----- CUSTOM EXCEPTION -----")


class InvalidMarks(Exception):
    pass


try:

    marks = int(input("Enter Marks: "))

    if marks > 100 or marks < 0:
        raise InvalidMarks("Marks should be between 0 and 100.")

    print("Valid Marks")

except InvalidMarks as e:
    print(e)


# ============================================================
# PRACTICE PROGRAM 1
# ============================================================

print("\n----- PRACTICE 1 -----")

try:
    num = int(input("Enter Number: "))
    print("Square =", num ** 2)

except ValueError:
    print("Invalid Number")


# ============================================================
# PRACTICE PROGRAM 2
# ============================================================

print("\n----- PRACTICE 2 -----")

try:
    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:
    print("Index does not exist.")


# ============================================================
# PRACTICE PROGRAM 3
# ============================================================

print("\n----- PRACTICE 3 -----")

try:
    data = {"Name": "Mansi"}

    print(data["Age"])

except KeyError:
    print("Key not found.")


# ============================================================
# MINI PROJECT
# ============================================================

print("\n========== SAFE CALCULATOR ==========")

try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    operator = input("Enter Operator (+,-,*,/): ")

    if operator == "+":
        print("Result =", num1 + num2)

    elif operator == "-":
        print("Result =", num1 - num2)

    elif operator == "*":
        print("Result =", num1 * num2)

    elif operator == "/":
        print("Result =", num1 / num2)

    else:
        print("Invalid Operator")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid Input")

finally:
    print("Calculator Closed.")


# ============================================================
# DAY 11 COMPLETED
# ============================================================

print("\n🎉 Congratulations!")
print("You have completed Day 11 - Exception Handling.")