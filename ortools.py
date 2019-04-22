from ortools.linear_solver import pywraplp


def main():
    solver = pywraplp.Solver(
        'Linear Example', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    solver.Solve()
