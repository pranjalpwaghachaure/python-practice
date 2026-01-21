# Practice: Input, Strings, and Basic Operations

# 1. Display user entered name followed by Good Afternoon
name = input("Enter your name: ")
print("Good Afternoon,", name)


# 2. Fill in a letter template with name and date
name = input("Enter your name: ")
date = input("Enter the date: ")

letter = f"""
Dear {name},
You are selected!
{date}
"""
print(letter)


# 3. Detect double space in a string
text = input("Enter a string: ")

if "  " in text:
    print("Double space detected")
else:
    print("No double space found")


# 4. Replace double space with single space
new_text = text.replace("  ", " ")
print("After removing double spaces:")
print(new_text)


# 5. Format letter using escape sequence characters
letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)
