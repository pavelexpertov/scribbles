from math import sqrt

def norm_l1(array):
    '''Return a Manahattan distance/length of a vector

    >>> norm_l1([0, 0, 0])
    0
    >>> norm_l1([5, -5])
    10
    >>> norm_l1([1, 2, 3])
    6
    >>> norm_l1([6, 7, 10])
    23
    '''
    return sum([abs(value) for value in array])

def norm_l2(array):
    '''Return an Euclidean distance/length of a vector

    >>> norm_l2([5, 5])
    7.0710678118654755
    >>> norm_l2([5, 5, 7, 14])
    17.175564037317667
    >>> norm_l2([-5, 5, -7, 14])
    17.175564037317667
    '''
    return sqrt(sum([value**2 for value in array]))

def max_norm(array):
    '''Return a length using maxnorm

    >>> max_norm([5, 5])
    5
    >>> max_norm([-6, 5])
    6
    >>> max_norm([5, 5, 7, 14])
    14
    >>> max_norm([5, 5, 7, 14, -52])
    52
    '''
    return max([abs(value) for value in array])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
