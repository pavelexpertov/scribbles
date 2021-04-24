import numpy

items_number = 10000000
array_1 = numpy.arange(items_number)
array_2 = numpy.arange(items_number)

def test():
    '''Test the numpy array with a huge line of itmes'''
    array_1.dot(array_2)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=50) )
