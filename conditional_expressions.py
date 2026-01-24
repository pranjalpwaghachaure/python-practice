# Practice: Conditional Expressions in Python


# 1. Find the greatest of four numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

greatest = max(a, b, c, d)
print("Greatest number is:", greatest)


# 2. Check pass or fail
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total_percentage = (m1 + m2 + m3) / 3

if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Student has passed")
else:
    print("Student has failed")


# 3. Detect spam comment
comment = input("Enter a comment: ")

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

if any(word in comment.lower() for word in spam_keywords):
    print("This is a spam comment")
else:
    print("This is not a spam comment")


# 4. Check username length
username = input("Enter username: ")

if len(username) < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains 10 or more characters")


# 5. Check if name is present in list
names = ["pranjal", "rahul", "amit", "sneha"]

name = input("Enter a name to search: ")

if name.lower() in names:
    print("Name is present in the list")
else:
    print("Name is not present in the list")


# 6. Calculate grade based on marks
marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


# 7. Check if post talks about Harry
post = input("Enter a post: ")

if "harry" in post.lower():
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")
