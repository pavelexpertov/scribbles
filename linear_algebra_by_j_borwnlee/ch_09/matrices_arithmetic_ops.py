def add_operation(A, B):
    '''Return a matrix with sums from two matrices.

    >>> add_operation([[1, 2, 3]], [[2, 3, 4]])
    [[3, 5, 7]]
    >>> add_operation([[1, 2, 3], [11, 12, 13]], [[2, 3, 4], [5, 6, 7]])
    [[3, 5, 7], [16, 18, 20]]
    '''
    new_matrix = []
    for a, b in zip(A, B):
        new_vector = [n1 + n2 for n1, n2 in zip(a, b)]
        new_matrix.append(new_vector)
    return new_matrix

def dot_product(A, B):
    '''Return a dot product of matrix

    >>> dot_product([[2, 3, 4]], [[1], [2]])
    Traceback (most recent call last):
    ValueError: A's n != B's m
    >>> dot_product([[2, 3, 4]], [[1]])
    Traceback (most recent call last):
    ValueError: A's n != B's m
    >>> dot_product([[2, 3, 4], [5, 6, 7], [8, 9, 10]], [[1], [2], [3]])
    [[20], [38], [56]]
    >>> dot_product([[2, 3, 4], [5, -6, 7], [8, 9, 10]], [[1], [2], [3]])
    [[20], [14], [56]]
    '''
    if len(A[0]) != len(B):
        raise ValueError("A's n != B's m")
    dot_product_matrix = []
    for m in A:
        vector = []
        for n in _get_columns(B):
            scalar = sum([scalar_1 * scalar_2 for scalar_1, scalar_2 in zip(m, n)])
            vector.append(scalar)
        dot_product_matrix.append(vector)
    return dot_product_matrix


def _get_columns(B):
    '''Generator to return 'column' with values'''
    item_length = len(B[0])
    column_counter = 0 # Counter to keep track of created 'columns'
    while(column_counter < item_length):
        column = []
        for item in B:
            column.append(item[column_counter])
        yield column
        column_counter += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
