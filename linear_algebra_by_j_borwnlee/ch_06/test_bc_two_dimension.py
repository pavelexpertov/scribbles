import numpy

import custom_broadcast as cb

def test():
    '''Test the numpy array with a huge line of itmes'''
    big_array = numpy.ones((100000, 2))
    cb.add_one_dimensional(big_array, [2, 6])


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=30) )
