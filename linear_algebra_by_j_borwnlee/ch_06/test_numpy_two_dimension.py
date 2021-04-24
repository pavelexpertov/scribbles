import numpy

def test():
    '''Test the numpy array with a huge line of itmes'''
    big_array = numpy.ones((100000, 2))
    big_array + numpy.array([2, 6])


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=30) )
