import sympy as sp
from sympy import symbols, sympify, SympifyError, Float

class CalculatorEvaluator:
    def __init__(self):
        self.variables = {}  # Dictionary to store user-defined variables

    def evaluate(self, expression):
        """
        Evaluate a mathematical expression using sympy.
        Supports variables, functions, and multi-operations.
        Handles assignments like 'x = 5' or 'f(x) = x**2'.
        """
        try:
            # Check if it's an assignment (e.g., 'x = 5')
            if '=' in expression:
                parts = expression.split('=', 1)
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    var_expr = parts[1].strip()
                    # Evaluate the right-hand side
                    rhs = sympify(var_expr, locals=self.variables)
                    # Store the variable
                    self.variables[var_name] = rhs
                    return f"{var_name} = {rhs}"
                else:
                    raise ValueError("Invalid assignment syntax")

            # Otherwise, evaluate the expression
            # Add float function to locals for explicit float conversion
            locals_dict = self.variables.copy()
            locals_dict['float'] = Float
            expr = sympify(expression, locals=locals_dict)
            result = expr.evalf()  # Evaluate to float for numerical results
            return str(result)

        except SympifyError as e:
            return f"Error: Invalid expression - {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_variables(self):
        """Return a string representation of current variables."""
        if not self.variables:
            return "No variables defined."
        return "\n".join([f"{k} = {v}" for k, v in self.variables.items()])
