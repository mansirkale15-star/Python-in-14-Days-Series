# ============================================================
# DAY 9 - Functions in Python
#
# Topics Covered:
# 1. Creating Functions
# 2. Calling Functions
# 3. Parameters
# 4. Arguments
# 5. Return Statement
# 6. Default Parameters
# 7. Keyword Arguments
# 8. *args
# 9. **kwargs
# 10. Lambda Functions
# 11. Recursion
# 12. Variable Scope
# ============================================================


# ============================================================
# SIMPLE FUNCTION
# ============================================================

print("----- SIMPLE FUNCTION -----")

def greet():
    print("Welcome to Python!")

greet()


# ============================================================
# FUNCTION WITH PARAMETERS
# ============================================================

print("\n----- FUNCTION WITH PARAMETERS -----")

def student(name):
    print("Student Name:", name)

student("Mansi")
student("Poonam")


# ============================================================
# MULTIPLE PARAMETERS
# ============================================================

print("\n----- MULTIPLE PARAMETERS -----")

def details(name, age):
    print("Name:", name)
    print("Age :", age)

details("Mansi", 19)


# ============================================================
# RETURN STATEMENT
# ============================================================

print("\n----- RETURN STATEMENT -----")

def add(a, b):
    return a + b

result = add(10, 20)

print("Addition =", result)


# ============================================================
# DEFAULT PARAMETERS
# ============================================================

print("\n----- DEFAULT PARAMETERS -----")

def country(name, nation="India"):
    print(name, "belongs to", nation)

country("Mansi")
country("John", "USA")


# ============================================================
# KEYWORD ARGUMENTS
# ============================================================

print("\n----- KEYWORD ARGUMENTS -----")

def employee(name, salary):
    print(name, salary)

employee(salary=50000, name="Raj")


# ============================================================
# *ARGS
# ============================================================

print("\n----- *ARGS -----")

def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))

total(10, 20)
total(10, 20, 30, 40, 50)


# ============================================================
# **KWARGS
# ============================================================

print("\n----- **KWARGS -----")

def information(**data):
    for key, value in data.items():
        print(key, ":", value)

information(Name="Mansi",
            Course="Data Science",
            City="Jalna")


# ============================================================
# LAMBDA FUNCTION
# ============================================================

print("\n----- LAMBDA FUNCTION -----")

square = lambda x: x*x

print(square(5))

addition = lambda a, b: a+b

print(addition(20, 30))


# ============================================================
# RECURSION
# ============================================================

print("\n----- RECURSION -----")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial =", factorial(5))


# ============================================================
# VARIABLE SCOPE
# ============================================================

print("\n----- VARIABLE SCOPE -----")

x = 100      # Global Variable

def demo():
    y = 50   # Local Variable
    print("Inside Function")
    print(x)
    print(y)

demo()

print("Outside Function")
print(x)


# ============================================================
# PRACTICE PROGRAM 1
# ============================================================

print("\n----- PRACTICE 1 -----")

def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(15)
even_or_odd(20)


# ============================================================
# PRACTICE PROGRAM 2
# ============================================================

print("\n----- PRACTICE 2 -----")

def largest(a, b):
    if a > b:
        return a
    return b

print("Largest =", largest(45, 78))


# ============================================================
# PRACTICE PROGRAM 3
# ============================================================

print("\n----- PRACTICE 3 -----")

def calculator(a, b):
    print("Addition =", a+b)
    print("Subtraction =", a-b)
    print("Multiplication =", a*b)
    print("Division =", a/b)

calculator(20, 5)


# ============================================================
# MINI PROJECT
# ============================================================

print("\n========== STUDENT RESULT ==========")

def student_result(name, marks):
    if marks >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    return result

name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

print("Student:", name)
print("Result :", student_result(name, marks))


# ============================================================
# DAY 9 COMPLETED
# ============================================================

print("\n🎉 Congratulations!")
print("You have completed Day 9 - Functions.")