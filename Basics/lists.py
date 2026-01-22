# 1. Remove duplicate elements from a list
numbers = []
n = int(input("Enter number of elements for the list: "))

for i in range(n):
    numbers.append(int(input(f"Enter element {i+1}: ")))

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List without duplicates:", unique_list)


# 2. Find largest and smallest number without using max() and min()
nums = [int(input("Enter a number: ")) for _ in range(5)]

largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


# 3. Count occurrences of an element in a list
elements = [1, 2, 3, 2, 4, 2, 5]
search = int(input("Enter element to count: "))

count = 0
for item in elements:
    if item == search:
        count += 1

print(f"{search} appears {count} times in the list")


# 4. Reverse a list without using reverse() or slicing
original_list = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(original_list)-1, -1, -1):
    reversed_list.append(original_list[i])

print("Original list:", original_list)
print("Reversed list:", reversed_list)


# 5. Separate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)