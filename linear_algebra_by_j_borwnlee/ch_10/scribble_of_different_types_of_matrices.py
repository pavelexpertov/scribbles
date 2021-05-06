'''Purpose of the module is to describe different matrix types in code'''

import numpy as np

# Setting default random generator
rng = np.random.default_rng(12345)

def get_square_matrix(m, n, random=False):
    '''Return a square matrix with integer scalaras. Whether random or not'''
    if m != n:
        raise ValueError(f"Rows and columns numbers don't match: {m} != {n}.")

    if random:
        return rng.integers(50, size=(m, n))
    else:
        return np.ones((m, n), dtype=int)

m = """
Square matrices are a type of matrices where column and row are equal.
(since it's a square Duh). These types of matrices allow to be used in
matrix arithmetic with ease due to equal sizes."""
