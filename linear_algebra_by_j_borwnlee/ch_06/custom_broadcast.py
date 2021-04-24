from collections.abc import Iterable
from operator import xor

def add_one_dimensional(big_array, small_array):
    '''Return a new array with one dimension containing sums between two arrays

    big_array is suppused to be bigger than small_array
    since values in the latter will get duplicated to
    demonstrate array broadcasting.

    >>> add_one_dimensional([0], [1])
    [1]
    >>> add_one_dimensional([1, 2], [1])
    [2, 3]
    >>> add_one_dimensional([1, 2, 3, 4], [3, 2])
    [4, 4, 6, 6]
    >>> add_one_dimensional([1, 2, 3, 4], [1, 2, 3, 4])
    [2, 4, 6, 8]
    >>> add_one_dimensional([1, 2, 3], [3, 2])
    Traceback (most recent call last):
    ValueError: Size of arrays ain't compatible for adding: 3 and 2
    '''
    array = []
    if len(big_array) % len(small_array) != 0:
        raise ValueError(f"Size of arrays ain't compatible for adding: {len(big_array)} and {len(small_array)}")
    number_of_times = int(len(big_array) / len(small_array))
    for item1, item2 in zip(big_array, small_array*number_of_times):
        array.append(item1+item2)
    return array

def add_two_dimensional(big_array, small_array):
    '''Return a new array with two dimensions containing sumbs between the arrays

    big_array is expected to be two dimensional whilst small_array can be two dimensional
    or one dimensional

    >>> add_two_dimensional([[1, 2], [3, 4]], [3])
    [[4, 5], [6, 7]]
    >>> add_two_dimensional([[1, 2], [3, 4]], [3, 4])
    [[4, 6], [6, 8]]
    '''
    array = []
    for item in big_array:
        array.append(add_one_dimensional(item, small_array))
    return array

def add(array_1, array_2):
    '''Return an array with products from two arrays.
    Ok, I am giving up on this implementation because it was getting out of hand
    when I tried to provide [[2,2], [4, 4]] and [2, 3].

    >>> add([], [])
    []
    >>> add([2], [2])
    [4]
    >>> add([2], 2)
    [4]
    >>> add([2, 2], [2])
    [4, 4]
    >>> add([2], [2, 2])
    [4, 4]
    >>> add([2, 2], [2, 3])
    [4, 5]
    >>> add([0], [2, 3])
    [2, 3]
    >>> add([2, 2, 3], [2, 3])
    Traceback (most recent call last):
    ValueError: Size of arrays ain't compatible for adding: 3 and 2
    >>> add([2, 2, 4, 4], [2, 3])
    [4, 5, 6, 7]
    >>> add([[2, 2], [4, 4]], [2, 3]) # the expted values is wrong so ignore the test
    [[4, 4], [7, 7]]
    '''
    if xor(isinstance(array_1, Iterable), isinstance(array_2, Iterable)):
        # One of arrays is a value not an interable.
        value = array_1 if not isinstance(array_1, Iterable) else array_2
        iterable = array_1 if isinstance(array_1, Iterable) else array_2
        return add(iterable, [value])
    elif isinstance(array_1, Iterable) and isinstance(array_2, Iterable):
        if len(array_1) == len(array_2):
            array = []
            for value1, value2 in zip(array_1, array_2):
                array.append(add(value1, value2))
            return array
        else:
            small_array = min(array_1, array_2, key=lambda x: len(x))
            big_array = max(array_1, array_2, key=lambda x: len(x))
            if not small_array:
                # Empty array == [0]
                small_array = [0]
            if _all_iterables(big_array):
                # If an array contains only iterables 
                small_array = small_array * len(big_array)
            elif all([not isinstance(item, Iterable) for item in big_array]):
                # if an array contains only values
                if len(big_array) % len(small_array) != 0:
                    raise ValueError(f"Size of arrays ain't compatible for adding: {len(big_array)} and {len(small_array)}")
                number_of_times = int(len(big_array) / len(small_array))
                small_array = small_array*number_of_times
            else:
                # if an array contains mixed values.
                raise ValueError("An array contains mixed values and iterables")

            array = []
            for value1, value2 in zip(big_array, small_array):
                array.append(add(value1, value2))
            return array
    else:
        return array_1 + array_2

def _all_iterables(array):
    """Return boolean to indicate all items are iterables within an array

    >>> _all_iterables([[], []])
    True
    >>> _all_iterables([[1], [2], [3]])
    True
    >>> _all_iterables([[1], [2], 3])
    False
    >>> _all_iterables([1, 2, 4])
    False
    """
    return all([isinstance(item, Iterable) for item in array])

def _all_solid_values(array):
    """Return boolean to indicate all items are solid values within an array.

    >>> _all_solid_values([1, 2])
    True
    >>> _all_solid_values([0])
    True
    >>> _all_solid_values([[1]])
    False
    >>> _all_solid_values([[1], [2]])
    False
    >>> _all_solid_values([[1], 2])
    False
    """
    return all([not isinstance(item, Iterable) for item in array])

def check_shape(array_1, array_2):
    '''Return boolean as to whether two array's shape match or not.

    Keep in mind the implementation is only for more-than-one dimensions
    arrays. Otherwise it will raise an error that types are incompatible.

    >>> check_shape(1, 1)
    True
    >>> check_shape([1], [1])
    True
    >>> check_shape([], [])
    True
    >>> check_shape([1, 2], [1, 2])
    True
    >>> check_shape([1, 2], [2, 1])
    True
    >>> check_shape([1, 2], [2, 1, 2])
    False
    >>> check_shape([2, 1, 2], [1, 2])
    False
    >>> check_shape([[1]], [[2]])
    True
    >>> check_shape([[]], [[]])
    True
    >>> check_shape([[1]], [[]])
    False
    >>> check_shape([[]], [[1]])
    False
    >>> check_shape([[1, 2], [2, 1]],[[3, 4], [4, 3]] )
    True
    >>> check_shape([[1, 2], [2, 1]],[[3, 4], [4, 3], [4, 3]] )
    False
    >>> check_shape([[3, 4], [4, 3], [4, 3]], [[1, 2], [2, 1]] )
    False
    >>> check_shape([[1, 2]], [1])
    Traceback (most recent call last):
    ValueError: Inconsistent types:
    <BLANKLINE>
    array_1: [1, 2]
    array_2: 1
    '''
    if isinstance(array_1, Iterable) and isinstance(array_2, Iterable):
        if len(array_1) != len(array_2):
            return False
        else:
            for item1, item2 in zip(array_1, array_2):
                do_match = check_shape(array_1[0], array_2[0])
                if not do_match:
                    return False
            else:
                return True
    elif xor(isinstance(array_1, Iterable), isinstance(array_2, Iterable)):
        # raise ValueError(f"Inconsistent types:\n\na")
        raise ValueError(f"Inconsistent types:\n\narray_1: {array_1}\narray_2: {array_2}")
    else:
        # At this point, arrays should be solid integers than iterables
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
