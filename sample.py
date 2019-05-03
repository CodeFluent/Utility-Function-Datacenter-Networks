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


# label the problem and choose finding maximum


# %%
from pulp import *
import numpy
prob = LpProblem("Giapetto", LpMaximize)

x1 = LpVariable("x1", lowBound=0, cat='Integer')  # Create a variable x1 >= 0
# Create another variable x2 >= 0
x2 = LpVariable("x2", lowBound=0, cat='Integer')
prob += 20*x1 + 30*x2  # Objective function
prob += 1*x1 + 2*x2 <= 100  # Finishing hours
prob += 2*x1 + 1*x2 <= 100  # Carpentry hours
prob  # Display the LP problem

# %%
status = prob.solve()  # Solve with the default solver
LpStatus[status]  # Print the solution status

# %%%
value(x1), value(x2), value(prob.objective)  # Show the solution
