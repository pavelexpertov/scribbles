'''Purpose of the module is to describe different matrix types in code'''

import numpy as np

# Setting default random generator
rng = np.random.default_rng(12345)

def get_square_matrix(m, n, random=False, integer=1):
    '''Return a square matrix with integer scalaras. Whether random or specified'''
    if m != n:
        raise ValueError(f"Rows and columns numbers don't match: {m} != {n}.")

    if random:
        return rng.integers(50, size=(m, n))
    else:
        return np.ones((m, n), dtype=int) * integer


if __name__ == "__main__":
    # Square matrix
    m = """
    Square matrices are a type of matrices where column and row are equal.
    (since it's a square Duh). These types of matrices allow to be used in
    matrix arithmetic with ease due to equal sizes."""
    print(m.strip())
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

