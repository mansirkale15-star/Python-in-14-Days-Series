# ============================================================
# DAY 2 - Conditional Statements
#
# Topics Covered:
# 1. Comparison Operators
# 2. if Statement
# 3. if-else Statement
# 4. if-elif-else Statement
# 5. Nested if
# 6. Logical Operators
# 7. Membership Operators
# 8. Grade Calculator
# 9. ATM Menu
# ============================================================


# ============================================================
# COMPARISON OPERATORS
# ============================================================

print("----- COMPARISON OPERATORS -----")

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ============================================================
# IF STATEMENT
# ============================================================

print("\n----- IF STATEMENT -----")

age = 20

if age >= 18:
    print("You are eligible to vote.")


# ============================================================
# IF ELSE
# ============================================================

print("\n----- IF ELSE -----")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ============================================================
# IF ELIF ELSE
# ============================================================

print("\n----- IF ELIF ELSE -----")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 35:
    print("Grade D")

else:
    print("Fail")


# ============================================================
# NESTED IF
# ============================================================

print("\n----- NESTED IF -----")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Incorrect Password")

else:
    print("Invalid Username")


# ============================================================
# LOGICAL OPERATORS
# ============================================================

print("\n----- LOGICAL OPERATORS -----")

age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")

if age < 18 or citizen:
    print("At least one condition is True")

if not False:
    print("NOT operator example")


# ============================================================
# MEMBERSHIP OPERATORS
# ============================================================

print("\n----- MEMBERSHIP OPERATORS -----")

fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)


print("========== ATM MENU ==========")

balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Available Balance: ₹", balance)

elif choice == "2":

    amount = float(input("Enter amount to deposit: "))
    balance += amount

    print("Deposit Successful")
    print("Updated Balance: ₹", balance)

elif choice == "3":

    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining Balance: ₹", balance)

    else:
        print("Insufficient Balance.")

elif choice == "4":
    print("Thank you for using our ATM.")

else:
    print("Invalid Choice.")
