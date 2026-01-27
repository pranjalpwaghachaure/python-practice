import random

def game(comp, user):
    if comp == user:
        return None

    if comp == 's':
        if user == 'w':
            return False
        elif user == 'g':
            return True

    if comp == 'w':
        if user == 'g':
            return False
        elif user == 's':
            return True

    if comp == 'g':
        if user == 's':
            return False
        elif user == 'w':
            return True


print("🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game")
print("Choose one:")
print("s → Snake")
print("w → Water")
print("g → Gun")

choices = ['s', 'w', 'g']
comp = random.choice(choices)

user = input("Enter your choice (s/w/g): ").lower()

result = game(comp, user)

print("\nComputer chose:", comp)
print("You chose:", user)

if result is None:
    print("🤝 It's a DRAW!")
elif result:
    print("🎉 You WIN!")
else:
    print("😢 You LOSE!")
