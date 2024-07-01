num = "1"

print(int(num))
print(
    int(float("1.2"))
)  # this is same as math.floor(float("1.2")). Better to use math.floor() way.
print(float(num))

# Boolean conversion takes truthy and falsy value
print(bool(""))  # False
print(bool("True"))  # True
print(bool("False"))  # True
print(bool("1"))  # True
print(bool("0"))  # True
print(bool(0))  # False
print(bool(1))  # True

try:
    print(int("1p"))
except Exception as e:
    (msg,) = e.args
    print("bruh", msg)


print("----Type of----")
print(type("1"))
print(type(1))
print(type(1.2))
