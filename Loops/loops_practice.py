# ============================
# LOOPS PRACTICE - PYTHON
# ============================

# 1. Print numbers from 1 to 10 using for loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 2. Print even numbers from 1 to 20
print("\n2. Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 3. Sum of first n natural numbers
n = int(input("\n3. Enter a number to find sum: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)


# 4. Multiplication table of a number
num = int(input("\n4. Enter a number for multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# 5. Print star pattern
# *
# **
# ***
print("\n5. Star Pattern:")
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)


# 6. Reverse counting using while loop
print("\n6. Reverse counting from 10 to 1:")
i = 10

while i >= 1:
    print(i)
    i -= 1


print("\n--- End of Loops Practice ---")
