import random

# value between 0 - 1
print(random.random())

# value between 0 - 100
print(round(random.random() * 100))  # Weird that round is global and not in math module

print(random.randrange(100, 200))
print(random.randrange(100, 200, 2))  # Only gives even value

# Shuffles mutates the original value
list = [1, 2, 3]
random.shuffle(list)
print(list)

print(random.choices([1, 2, True, "Sike"])[0])  # random.choices() returns an array
