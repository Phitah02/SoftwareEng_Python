### README for Basic Scientific Calculator

#### Overview
This Python script implements a versatile scientific calculator capable of performing arithmetic operations, trigonometric functions, logarithms, calculus (differentiation and integration), algebraic equation solving, matrix/vector operations, and 2D/3D plotting.

#### Features
1. **Basic Arithmetic**:
   - Addition, subtraction, multiplication, division
   - Error handling for division by zero

2. **Scientific Functions**:
   - Exponentiation and square roots
   - Trigonometric functions (sine, cosine, tangent) with degree inputs
   - Logarithms (base 10 and natural)

3. **Calculus**:
   - Symbolic differentiation
   - Symbolic integration

4. **Algebra**:
   - Equation solving (e.g., `x**2 - 4 = 0`)

5. **Linear Algebra**:
   - Matrix operations (addition, multiplication, transpose)
   - Vector operations (dot product, cross product)

6. **Data Visualization**:
   - 2D function plotting
   - 3D surface plotting

#### Dependencies
- Python 3.x
- Required libraries:
  ```bash
  numpy sympy matplotlib
  ```
  Install with:  
  `pip install numpy sympy matplotlib`

#### Usage
Run the script and select an operation from the menu:
```bash
python My_calc.py
```

**Example Workflow**:
1. Choose operation (1-18)
2. Provide inputs as prompted:
   - For calculus/algebra: Enter expressions like `x**2 + 3*x`
   - For plots: Enter expressions like `x**2 + y**2`
3. View results in console or graphical plots

#### Notes
- **Trigonometric functions** expect angles in **degrees**
- Logarithm functions require positive inputs
- Plots automatically generate with customizable ranges
- Uses symbolic computation (`sympy`) for calculus/algebra

#### Safety
⚠️ **Important**: This script uses `eval()` for symbolic operations. Only run with trusted mathematical expressions. Do not use for untrusted inputs.

