
def add(l1, l2):
    return [x + y for x, y in zip(l1, l2)]


def minus(l1, l2):
    return [x - y for x, y in zip(l1, l2)]

def multiply(l1, l2):
    return [x * y for x, y in zip(l1, l2)]

def divide(l1, l2):
    return [x / y for x, y in zip(l1, l2)]

def dot_product(l1, l2):
    products = multiply(l1, l2)
    return sum(products)
