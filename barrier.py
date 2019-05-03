# %%
from cvxopt import lapack, solvers, matrix, spdiag, log, div, normal
from cvxopt.modeling import variable, op, max, min, sum
from array import array
import numpy as np

j = 10  # number of datacenters
k = 100  # number of jobs each containing t tasks


c1 = []  # input data size
c2 = []  # link bandwidth
c3 = []  # execution time
c4 = []  # communication time
c5 = []  # resource capacity

m = j + k
n = j * k

TMU = np.zeros(shape=(m, n), dtype=int)

# an m x n matrix representing the constraints 5 (computational resource exceed) and constraints 6
# (each job assigned to at least 1 datacenter)
A = matrix(np.array(TMU), tc='i')
print(A)

# %%


def centering():

    pass


# %%
def solve():
    pass
