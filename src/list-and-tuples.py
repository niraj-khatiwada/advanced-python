list = [1, 2, 3]
list[0] = 100
list[1] = 200
list[2] = 300

print(list)
print(len(list))

# push
list.append(400)
print(list)
# push multiple items. .push(...[400, 500]) in JavaScript
list.extend([500, 600])

# pop
list.pop()
print(list)

# Like splice but just for insert
list.insert(3, 500)
print(list)

# Remove by item not by index
list.remove(100)
print(list)

# indexOf. Throws exception if item is not present
print(list.index(200))

# Slice
# [start:stop:step]
print(list[1:-1])

# Reverse
print("Reverse is", [1, 2, 3][::-1])
print("Reverse is", ["a", "b", "c"][::-1])

print("------------")

# Tuples
# Tuples ar readonly
tuple = (1, 2, 3)
print(tuple)
print(tuple[0])
print(tuple)
