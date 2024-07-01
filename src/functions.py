def sum_product(a, b, c=None):
    return (a + b + (0 if c is None else c), a * b * (1 if c is None else c))


sum, product = sum_product(b=2, a=2, c=100)
print(sum, product)
