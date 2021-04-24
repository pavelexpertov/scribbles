import vector_arithmetic as va

items_number = 10000000
array_1 = [number for number in range(items_number)]
array_2 = [number for number in range(items_number)]

def test():
    '''Test the numpy array with a huge line of itmes'''
    va.dot_product(array_1, array_2)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=50) )
