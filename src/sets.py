# Set Initialization
s = set()
s.add(1)
s.add(1)
s.add(2)

print(s)
print(type(s))

s.remove(1)
print(s)

if 3 in s:
    s.remove(3)
print(s)


# Set literals
print("---- Set Literals----")
sl = {1, 2, 3, 1}
print(sl)
print(type(sl))
