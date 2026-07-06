# ============================================================
# DAY 3 - Loops
#
# Topics Covered:
# 1. for Loop
# 2. range()
# 3. while Loop
# 4. break
# 5. continue
# 6. pass
# 7. Nested Loops
# ============================================================


# ============================================================
# FOR LOOP
# ============================================================

print("----- FOR LOOP -----")

for i in range(1, 6):
    print(i)


# ============================================================
# RANGE FUNCTION
# ============================================================

print("\n----- RANGE FUNCTION -----")

print("range(5)")
for i in range(5):
    print(i)

print("\nrange(2, 8)")
for i in range(2, 8):
    print(i)

print("\nrange(1, 11, 2)")
for i in range(1, 11, 2):
    print(i)


# ============================================================
# WHILE LOOP
# ============================================================

print("\n----- WHILE LOOP -----")

count = 1

while count <= 5:
    print(count)
    count += 1


# ============================================================
# BREAK
# ============================================================

print("\n----- BREAK -----")

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# ============================================================
# CONTINUE
# ============================================================

print("\n----- CONTINUE -----")

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# ============================================================
# PASS
# ============================================================

print("\n----- PASS -----")

for i in range(5):

    if i == 3:
        pass

    print(i)


# ============================================================
# NESTED LOOP
# ============================================================

print("\n----- NESTED LOOP -----")

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)



print("----- PATTERN PRINTING -----")

rows = 5

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end=" ")

    print()

# ---------------- Number Guessing Game ----------------

secret_number = 7

while True:

    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")

# ---------------- Multiplication Table ----------------

number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}\n")

for i in range(1, 11):

    print(f"{number} x {i} = {number * i}")


print("----- COUNTDOWN -----")

count = 10

while count >= 1:
    print(count)
    count -= 1

print("🎉 Time's Up!")