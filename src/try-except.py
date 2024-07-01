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
# If no error was thrown then it;s better to process in try: block. So this else is usually not used.
else:
    print("NO EXCEPTION WAS THROWN")
finally:
    print("Task complete")
