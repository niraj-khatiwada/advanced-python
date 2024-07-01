name = " Niraj"

print(len(name))
print(name.strip())
print(name.startswith("N"))
print(name.endswith("N"))
print(name.find("X"))
print("Replaced: ", name.replace("Niraj", "N"))
print(
    ".".join(["a", "b", "c"])
)  # a.b.c This is equivalent to ["a", "b", "c"].join(".") in JavaScript.

print(name.upper())
print(name.lower())
print("niraj".capitalize())
print(name.split(" "))
print(name.find("-"))
print(
    name.index(" ")
)  # index and find both finds the index of first match but this one throws error when item is not found whereas find() returns -1. Prefer using find() instead of this.

print("banana".count("a"))  # Count of occurrence of the string inside a string

# Slice in python
print("Niraj K"[1:-1])


# Gives ascii value
print(ord("a"))  # ord stands for ordinal
print(ord("A"))

print("a" < "A")  # This is compared based on the ascii code
