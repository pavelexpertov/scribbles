# coding: utf-8
from numpy import array
from numpy.linalg import norm
from numpy import inf
def print_ls(ar):
    print("The array:", ar)
    print("l1:", norm(ar, 1))
    print("l2:", norm(ar, 2))
    print("maxnnorm:", norm(ar, inf))
    
