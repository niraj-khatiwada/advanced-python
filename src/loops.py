print("---Range---")
print(range(10))  # 0-10. 10 is exclusive. So image it to be 0-9
print(range(10)[1:-1])  # 1-9 ~ 1-8


for i in range(10):
    print(i)


# Steps
print(range(0, 10, 2))  # Start, Stop, Step. The `Stop` value is always exclusive.

for i in range(0, 10, 2):
    print(i)

# Reverse
print("---Reverse---")
for i in range(10, 0, -1):
    print(i)


print("---List---")
for i in [1, 3, 4]:
    print(i)

# Including index:
list = [1, 3, 4]
for index in range(len(list)):
    print(index, list[index])

print("----Enumerate----")
# Or you can use enumerate
for index, val in enumerate([4, 5, 6]):
    print(index, val)
