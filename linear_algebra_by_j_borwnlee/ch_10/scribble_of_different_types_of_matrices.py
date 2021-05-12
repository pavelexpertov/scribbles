'''Purpose of the module is to describe different matrix types in code'''

import numpy as np

# Setting default random generator
rng = np.random.default_rng(12345)

def get_square_matrix(n, random=False, integer=1):
    '''Return a square matrix with integer scalaras. Whether random or specified'''

    if random:
        return rng.integers(50, size=(n, n))
    else:
        return np.ones((n, n), dtype=int) * integer

def get_symmetrical_matrix(n):
    '''Return a matrix that's symetrical'''
    # Creating permutations of rows
    current_integer_list = [i for i in range(1, n+1)]
    permutations = []
    while(current_integer_list[-1] != 1):
        permutations.append(current_integer_list[:])
        current_integer_list.pop()
        current_integer_list.insert(0, current_integer_list[0] + 1)
    # To add the last row
    permutations.append(current_integer_list[:])
    return np.array(permutations)

def get_triangular_matrix(matrix, triangular_type):
    '''Return a triangular matrix'''
    if triangular_type == "triup":
        return np.triu(matrix)
    elif triangular_type == "trile":
        return np.tril(matrix)
    else:
        raise ValueError("'tringular_type' is either wrong or empty.")

def format_message_str(string):
    '''Return re-formated string for output messages.

    It's expected a docstring with 4 spaces that delimits sentences
    with some new lines at each end.
    '''
    string = string.strip()
    return "\n".join([line.strip() for line in string.split(" "*4)])

if __name__ == "__main__":
    # Square matrix
    m = """
    Square matrices are a type of matrices where column and row are equal.
    (since it's a square Duh). These types of matrices allow to be used in
    matrix arithmetic with ease due to equal sizes."""
    print(format_message_str(m))
    print('4 x 4 square matrix')
    print(get_square_matrix(4, 4, True))
    print("Let's do some square matrix arithmetic")
    A = get_square_matrix(5, 5, integer=2)
    B = get_square_matrix(5, 5, integer=5)
    print('A:\n', A)
    print('B:\n', B)
    print("Let's do some multiplication and division in the form of A * B and A / B")
    print("Multiplication:\n", A * B)
    print("Division:\n", A / B)
    print("Keep in mind that it multiplies across elements, not dot products")
    # Symmetrical matrix
    m = """
    Symmetrical matrix is a square matrix that has values mirrored along a diagonal line.
    The diagonal line consists of just '1' scalars and then each scalar get's incremented to left and right
    sides of the diagonal line.
    For example, a matrix with 16 dimension size would look like this:
    """
    print(format_message_str(m))
    print("\n", get_symmetrical_matrix(16))
    print("It has to be a square such that the values can be mirrored")

    # Triangular matrix
    m = """
    Triangular matrix is a square matrix where a part of matrix
    (in a shape of a 'square') has values on one side of diagonal
    line and the other one has zeros.

    Triangular matrix can be characterised by either 'triangular up' (scalar values above
    diagonal line) and 'triangular down' (scalar values below diagonal line).

    For example a 5x5 trinagular matrix would like this:
    """
    print(format_message_str(m))
    m = get_square_matrix(5, random=True)
    print(get_triangular_matrix(m, "trile"))
    print("or this:")
    print(get_triangular_matrix(m, "triup"))
    m = """
    Functions that can perform the formatting of these matrices are `numpy.tril`
    and `numpy.triu`.
    """
    print(format_message_str(m))
    # Diagonal matrix
    # Identity matrix
    # Orthogonal matrix
