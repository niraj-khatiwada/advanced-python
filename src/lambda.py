import functools

_sum = lambda a, b: a + b
print(_sum(1, 2))

array = [1, 2, 3, 4, 5]
# Map
mapped = map(lambda x: f"{x}", array)
print(type(mapped), type(mapped).__name__ == "map")
print(list(mapped))

# Filter
filtered = filter(lambda x: x % 2 == 0, array)
print(type(filtered), type(filtered).__name__ == "filter")
print(list(filtered))

# Reduce
reduced = functools.reduce(lambda a, c: a + c, array)
print(type(reduced))  # Type changes based on return value of reduce.Here it is `int`
print(reduced)

reduced = functools.reduce(lambda a, c: f"{a}{c}", array)
print(type(reduced))  # Here it is `str`
print(reduced)
