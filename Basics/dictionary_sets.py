# Practice: Dictionary and Sets in Python


# 1. Hindi to English dictionary lookup
hindi_dict = {
    "namaste": "Hello",
    "pani": "Water",
    "kitab": "Book",
    "kursi": "Chair"
}

word = input("Enter a Hindi word: ")
print("Meaning:", hindi_dict.get(word, "Word not found"))


# 2. Input 8 numbers and display unique numbers
numbers = set()

for i in range(8):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Unique numbers are:", numbers)


# 3. Can a set have 18 (int) and '18' (str)?
test_set = {18, '18'}
print(test_set)


# 4. Length of set after operations
s = set()
s.add(20)
s.add(20.0)
s.add('20')

print("Set s:", s)
print("Length of s:", len(s))  # Answer: 2


# 5. Type of empty braces
s = {}
print("Type of s:", type(s))  # dict


# 6. Favorite language dictionary
fav_lang = {}

for i in range(4):
    name = input("Enter friend's name: ")
    lang = input("Enter favorite language: ")
    fav_lang[name] = lang

print("Favorite languages:", fav_lang)



