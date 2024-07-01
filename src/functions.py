def sum_product(a, b, c=None):
    return (a + b + (0 if c is None else c), a * b * (1 if c is None else c))


sum, product = sum_product(b=2, a=2, c=100)
print(sum, product)

# Unpack: You can unpack elements from array into positional arguments
print("Unpacked", sum_product(*[1, 2]))


def sum(*args):
    print("ARGS", args, type(args))  # Args are tuples
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum


print(sum(1, 2, 3))


def product(**kwargs):
    print("KWARGS", kwargs, type(kwargs))  # kwargs are dictionaries
    product = 1
    for i in kwargs:
        product *= kwargs[i]
    return product


print(product(a=1, b=2, c=3))


def advanced_sum(*args, **kwargs):
    sum = 0
    for i in range(len(args)):
        sum += args[i]

    for key in kwargs:
        sum += kwargs[key]

    return sum


print(
    "Advanced sum", advanced_sum(1, 2, a=2, b=4)
)  # Positional arguments should always be present at the last
