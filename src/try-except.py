def sum(a, b):
    if type(a).__name__ == "str":
        raise Exception("Invalid value supplied `a`.")
    if type(b).__name__ == "str":
        raise Exception("Invalid value supplied `b`.")
    return a + b


s = 0

try:
    s = sum("1", 2)
except Exception as e:
    print("Oops something went wrong= ", e)
finally:
    print("Task complete")
