# Functions and Recursion Practice
# Author: Pranjal Waghachaure

# 1. Greatest of three numbers
def greatest(a, b, c):
    return max(a, b, c)

print("Greatest:", greatest(10, 20, 15))


# 2. Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("Fahrenheit:", celsius_to_fahrenheit(37))


# 3. Prevent print() from printing a new line
print("Hello", end=" ")
print("World")


# 4. Recursive sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))


# 5. Pattern printing
def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

pattern(3)


# 6. Inches to centimeters
def inches_to_cm(inch):
    return inch * 2.54

print("5 inches in cm:", inches_to_cm(5))


# 7. Remove a word from list and strip spaces
def remove_and_strip(word, lst):
    return [item.strip() for item in lst if item.strip() != word]

names = [" Ram ", " Shyam ", " Hari "]
print(remove_and_strip("Hari", names))


# 8. Multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)
