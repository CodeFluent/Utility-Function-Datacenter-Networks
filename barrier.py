# %%
from cvxopt import lapack, solvers, matrix, spdiag, log, div, normal, uniform, blas
from cvxopt.modeling import variable, op, max, min, sum
from array import array
from operator import mul
from math import sqrt
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
b = uniform(m, 1)

# Make x = 0 feasible for  barrier. A flow can be allocated 0 time in favor of antoher getting more time. b is always positive.
b /= (1.1 * max(abs(b)))


# %%

"""
Centering uses Newton's Centering Method. This part is from the example given by cvxopt library. 

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

    for iter in range(MAXITERS):
        print(x)
        # get the gradient of the function
        d = (b - A*x) ** - 1
        g = A.T * d

        # get Hessian
        # lower diaganol multiplied to constraint matrix
        h = mul(d[:, n*[0]], A)
        # use the BLAS solver to get the symmetric matrix and get roots
        blas.syrk(h, H, trans='T')

        # do Newton's step
        v = -g  # g is our gradient
        # LAPACK solves the matrix and gives us the tep value to transverse with
        lapack.posv(H, v)

        # Stop condition if exceeding tolerance
        lam = blas.dot(g, v)
        if sqrt(-lam) < mu:
            return x  # return the orignal value if we're above tolerance

        # Line search to go to optimal using ALPHA and BETA
        y = mul(A * v, d)
        step = 1.0
        while 1 - step*max(y) < 0:
            step *= BETA
        while True:
            if -sum(log(1 - step*y)) < (ALPHA * step * lam):
                break
            step *= BETA

        # increment x by the step times the negative gradient otherwise
        x += step*v


# %%
def solve():
    pass


centering()
