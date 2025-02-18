from sympy import symbols, Eq, solve

# Define variables for steady-state probabilities
pi1, pi2, pi3 = symbols('pi1 pi2 pi3')

# Define the system of equations based on πP = π
eq1 = Eq(pi1 - (1/2)*pi1 - (1/3)*pi2 - (1/2)*pi3, 0)
eq2 = Eq(pi2 - (1/4)*pi1 - (1/2)*pi3, 0)
eq3 = Eq(pi3 - (1/4)*pi1 - (2/3)*pi2, 0)
eq4 = Eq(pi1 + pi2 + pi3, 1)  # Normalization condition

# Solve the system of equations
solution = solve((eq1, eq2, eq3, eq4), (pi1, pi2, pi3))
print(solution)
