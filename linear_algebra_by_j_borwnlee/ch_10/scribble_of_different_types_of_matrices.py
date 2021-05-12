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

def format_message_str(string):
    '''Return re-formated string for output messages.

    It's expected a docstring with 4 spaces that delimits sentences
    with some new lines at each end.
    '''
    string = string.strip()
    return "\n".join(string.split(" "*4))

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
    
    # Diagonal matrix
    # Identity matrix
    # Orthogonal matrix
