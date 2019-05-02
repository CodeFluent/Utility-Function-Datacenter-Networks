'''
    From: https://github.com/yongtwang/engineering-python/blob/master/18B_Linear_Programming_using_PuLP/18B_Linear_Programming_using_PuLP.ipynb

    Trying out python pulp and doing Giapetto's LP problem.

'''

'''
Giapetto's Problem:

    Giapetto, Inc. manufactures two types of furniture: chairs and tables. 
    The manufacturer wants to maximize their weekly profit.

    - $20 of profit per chair.
    - $30 of profit per table.
    - A chair requires 1 hour of finishing labor and 2 hours of carpentry labor.
    - A table requires 2 hours of finishing labor and 1 hour of carpentry labor.

    - Each week, Giapetto has only 100 finishing hours and 100 carpentry hours 
    available.

    This means we are using objective function:
            
            max z = 20x + 30y

    with constraints:
        Finishing Labor Constraint: x + 2y
        Carprentry Labor Constraint: 2x + y




'''


from pulp import *
import numpy


# label the problem and choose finding maximum
prob = LpProblem("Giapetto", LpMaximize)

