# 1. Find sum and average of tuple elements
t = (10, 20, 30, 40, 50)
total = 0

for num in t:
    total += num

average = total / len(t)

print("Tuple:", t)
print("Sum:", total)
print("Average:", average)


# 2. Find maximum and minimum in a tuple
tup = (5, 8, 2, 10, 3)
max_val = tup[0]
min_val = tup[0]

for num in tup:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Maximum value:", max_val)
print("Minimum value:", min_val)


# 3. Convert tuple to list, modify it, and convert back
tuple_data = (1, 2, 3, 4)
list_data = list(tuple_data)

list_data.append(5)

tuple_data = tuple(list_data)
print("Modified tuple:", tuple_data)


# 4. Check if an element exists in a tuple
tup = (10, 20, 30, 40)
element = int(input("Enter element to search in tuple: "))

if element in tup:
    print("Element found in tuple")
else:
    print("Element not found in tuple")


# 5. Count even and odd numbers in a tuple
numbers = (1, 2, 3, 4, 5, 6)
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)