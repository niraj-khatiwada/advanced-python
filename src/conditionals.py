import random

# Equivalent to &&
is_true = 1 > 2 and 2 < 3
print(is_true)

# Equivalent to ||
is_true = 1 < 2 or 22 > 3
print(is_true)

# Equivalent to !
is_true = not (1 > 2)
print(is_true)
print(not True)

# Similar Ternary Operator
print(True if random.random() < 0.5 else False)  # random.random() < 0.5 ? True : False
