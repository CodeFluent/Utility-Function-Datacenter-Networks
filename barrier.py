# %%
from cvxopt import lapack, solvers, matrix, spdiag, log, div, normal, uniform, blas
from cvxopt.modeling import variable, op, max, min, sum
from array import array
from operator import mul
import numpy as np


mu = 2e-01  # tolerance for barrier function


j = 10  # number of datacenters
k = 5  # number of jobs each containing t tasks


c1 = []  # input data size
c2 = []  # link bandwidth
c3 = []  # execution time
c4 = []  # communication time
c5 = []  # resource capacity

m = j + k
n = j * k

TMU = np.zeros(shape=(m, n), dtype=int)  # a totally unimodular matrix of zeros

# an m x n matrix representing the constraints 5 (computational resource exceed) and constraints 6
# (each job assigned to at least 1 datacenter)
A = matrix(np.array(TMU), tc='i')

# b is our value that x can reach given constraints of A.
b = uniform(m, n, 0, 1)

# Make x = 0 feasible for  barrier. A flow can be allocated 0 time in favor of antoher getting more time. b is always positive.
b /= (1.1 * max(abs(b)))


# %%

"""
Centering uses Newton's Centering Method. This part is similar to the example given by cvxopt library. 

We are given mu by the tolerance above. If any centering reaches close to mu we stop since that is close to the 
edge of non-feasible solutions and exterior to any optimal solution.

"""


def centering():

    # variables kept same from cvxopt example
    MAXITERS = 100
    ALPHA = 0.01
    BETA = 0.5

    x = matrix(0.0, (n, 1))
    H = matrix(0.0, (n, n))  # Symmetrix matrix

    for iter in xrange(MAXITERS):

        # get the gradient of the function
        d = (b - A*x) ** - 1
        g = A.T * d

        # get Hessian
        # lower diaganol multiplied to constraint matrix
        h = mul(d[:, n*[0]], A)
        blas.syrk(h, H, trans='T')  # use the BLAS solver

    pass


# %%
def solve():
    pass
