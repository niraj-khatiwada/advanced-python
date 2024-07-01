object = {"a": 1, "b": 2}

print(object)
print(type(object))

# Get
print(object["a"])

# Set
object["b"] = 3
object["c"] = 4
print(object)

# Exists
print("a" in object)


# Keys, Values and Entries
print(object.keys())
for key in object.keys():
    print(key)

print(object.values())
for value in object.values():
    print(value)

for key, value in object.items():
    print(key, value)

# Convert keys, values into a list
print(list(object.keys()))
print(list(object.values()))


# Delete a value
del object["a"]

if "z" in object:
    del object["z"]

print(object)
