'''PETER KAMAU MWAURA'''
import math
import numpy as np
from sympy import symbols, diff, integrate, Eq, solve, Matrix
import matplotlib.pyplot as plt
from sympy import lambdify

# Basic arithmetic functions
# These functions perform addition, subtraction, multiplication, and division.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error: Division by zero'
    return x / y

# Scientific functions
# Power, square root, trigonometric, and logarithmic functions using math library.
def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def sine(x):
    # Converts degrees to radians before calculating sine
    return math.sin(math.radians(x))

def cosine(x):
    # Converts degrees to radians before calculating cosine
    return math.cos(math.radians(x))

def tangent(x):
    # Converts degrees to radians before calculating tangent
    return math.tan(math.radians(x))

def logarithm(x, base=10):
    # Checks for valid input before calculating logarithm
    if x <= 0:
        return 'Error: Logarithm undefined for non-positive values'
    return math.log(x, base)

# Natural logarithm function
# Returns the natural logarithm (base e) of x
def natural_log(x):
    if x <= 0:
        return 'Error: Logarithm undefined for non-positive values'
    return math.log(x)

# Differentiation function
# Returns the derivative of a given expression with respect to a variable
def differentiate(expr, var):
    return diff(expr, var)

# Integration function
# Returns the integral of a given expression with respect to a variable
def integrate_expr(expr, var):
    return integrate(expr, var)

# Algebra solver
# Solves algebraic equations
def solve_equation(equation, var):
    return solve(equation, var)

# Matrix operations
# Returns the sum, product, and transpose of matrices
def matrix_operations():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    return {
        'sum': A + B,
        'product': A * B,
        'transpose_A': A.transpose()
    }

# Vector operations
# Returns the dot product and cross product of vectors
def vector_operations():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    return {
        'dot': np.dot(v1, v2),
        'cross': np.cross(v1, v2)
    }

# 2D plot function
# Plots a 2D graph of a given expression in terms of x
def plot_2d(expr_str):
    x = symbols('x')
    expr = eval(expr_str)
    f = lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals)
    plt.title(f"2D Plot of {expr_str}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# 3D plot function
# Plots a 3D graph of a given expression in terms of x and y
def plot_3d(expr_str):
    x, y = symbols('x y')
    expr = eval(expr_str)
    f = lambdify((x, y), expr, modules=['numpy'])
    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(f"3D Plot of {expr_str}")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

if __name__ == "__main__":
    print("Mini Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Natural Logarithm")
    print("12. Differentiate")
    print("13. Integrate")
    print("14. Solve Algebraic Equation")
    print("15. Matrix Operations")
    print("16. Vector Operations")
    print("17. Plot 2D Graph")
    print("18. Plot 3D Graph")
    choice = input("Enter choice (1-18): ")

    # Arithmetic operations
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            # Addition
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            # Subtraction
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            # Multiplication
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            # Division
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            # Power
            print("Result:", power(num1, num2))
    # Square root
    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result:", sqrt(num))
    # Sine function
    elif choice == '7':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", sine(angle))
    # Cosine function
    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", cosine(angle))
    # Tangent function
    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", tangent(angle))
    # Logarithm function
    elif choice == '10':
        num = float(input("Enter number: "))
        base = input("Enter base (default 10): ")
        base = float(base) if base else 10
        print("Result:", logarithm(num, base))
    # Natural logarithm
    elif choice == '11':
        num = float(input("Enter number: "))
        print("Result:", natural_log(num))
    # Differentiation
    elif choice == '12':
        expr_str = input("Enter expression (e.g., x**2 + 3*x): ")
        var_str = input("Differentiate with respect to (e.g., x): ")
        var = symbols(var_str)
        expr = eval(expr_str)
        print("Result:", differentiate(expr, var))
    # Integration
    elif choice == '13':
        expr_str = input("Enter expression (e.g., x**2 + 3*x): ")
        var_str = input("Integrate with respect to (e.g., x): ")
        var = symbols(var_str)
        expr = eval(expr_str)
        print("Result:", integrate_expr(expr, var))
    # Algebraic equation solver
    elif choice == '14':
        eq_str = input("Enter equation (e.g., x**2 - 4): ")
        var_str = input("Solve for (e.g., x): ")
        var = symbols(var_str)
        equation = Eq(eval(eq_str), 0)
        print("Result:", solve_equation(equation, var))
    # Matrix operations
    elif choice == '15':
        results = matrix_operations()
        print("Matrix Sum:\n", results['sum'])
        print("Matrix Product:\n", results['product'])
        print("Transpose of Matrix A:\n", results['transpose_A'])
    # Vector operations
    elif choice == '16':
        results = vector_operations()
        print("Dot Product:", results['dot'])
        print("Cross Product:", results['cross'])
    # 2D Plot
    elif choice == '17':
        expr_str = input("Enter expression in x (e.g., x**2 + 3*x): ")
        plot_2d(expr_str)
    # 3D Plot
    elif choice == '18':
        expr_str = input("Enter expression in x and y (e.g., x**2 + y**2): ")
        plot_3d(expr_str)
    else:
        print("Invalid input")
