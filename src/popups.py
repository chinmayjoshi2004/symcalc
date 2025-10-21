import tkinter as tk
from tkinter import ttk, scrolledtext, Toplevel, messagebox

def insert_text_to_entry(gui_instance, text):
    current = gui_instance.input_entry.get("1.0", tk.END).rstrip('\n')
    gui_instance.input_entry.delete("1.0", tk.END)
    gui_instance.input_entry.insert("1.0", current + text)

def clear_entry(gui_instance):
    gui_instance.input_entry.delete("1.0", tk.END)

def calculate(gui_instance):
    expression = gui_instance.input_entry.get("1.0", tk.END).strip()
    if expression:
        result = gui_instance.evaluator.evaluate(expression)
        formatted_result = format_result(result)
        # Clear welcome message on first calculation
        if gui_instance.first_calculation:
            gui_instance.results_display.config(state=tk.NORMAL)
            gui_instance.results_display.delete("1.0", tk.END)
            gui_instance.results_display.config(state=tk.DISABLED)
            gui_instance.first_calculation = False
        # Only add to history if the result differs from the input expression
        if formatted_result != expression:
            gui_instance.results_display.config(state=tk.NORMAL)
            gui_instance.results_display.insert(tk.END, f"> {expression} = {formatted_result}\n\n")
            gui_instance.results_display.see(tk.END)
            gui_instance.results_display.config(state=tk.DISABLED)
        gui_instance.input_entry.delete("1.0", tk.END)
        gui_instance.input_entry.insert("1.0", formatted_result)

def format_result(result):
    try:
        num = float(result)
        if num.is_integer():
            return str(int(num))
        else:
            return f"{num:.4f}".rstrip('0').rstrip('.')
    except ValueError:
        return str(result)

def toggle_theme(gui_instance):
    gui_instance.toggle_theme()

def show_variables(gui_instance):
    vars_str = gui_instance.evaluator.get_variables()
    gui_instance.results_display.config(state=tk.NORMAL)
    gui_instance.results_display.insert(tk.END, f"Variables:\n{vars_str}\n\n")
    gui_instance.results_display.see(tk.END)
    gui_instance.results_display.config(state=tk.DISABLED)

def show_history_popup(gui_instance):
    popup = Toplevel(gui_instance.root)
    popup.title("Calculation History")
    popup.geometry("600x400")
    popup.configure(bg=gui_instance.colors['background'])

    history_text = scrolledtext.ScrolledText(popup, font=('Consolas', 10), bg=gui_instance.colors['surface_secondary'], fg=gui_instance.colors['text'])
    history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    history_content = gui_instance.history.get("1.0", tk.END)
    history_text.insert(tk.END, history_content)
    history_text.config(state=tk.DISABLED)

def show_help_popup(gui_instance):
    popup = Toplevel(gui_instance.root)
    popup.title("Help")
    popup.geometry("700x500")
    popup.configure(bg=gui_instance.colors['background'])

    help_text = scrolledtext.ScrolledText(popup, font=('Consolas', 10), bg=gui_instance.colors['surface_secondary'], fg=gui_instance.colors['text'])
    help_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    help_content = get_help_content()
    help_text.insert(tk.END, help_content)
    help_text.config(state=tk.DISABLED)

def show_settings_popup(gui_instance):
    popup = Toplevel(gui_instance.root)
    popup.title("Settings")
    popup.geometry("400x300")
    popup.configure(bg=gui_instance.colors['background'])

    theme_label = tk.Label(popup, text="Theme:", font=('Segoe UI', 12), bg=gui_instance.colors['background'], fg=gui_instance.colors['text'])
    theme_label.pack(pady=20)

    theme_button = tk.Button(popup, text="Toggle Theme", command=lambda: toggle_theme(gui_instance), bg=gui_instance.colors['primary'], fg='white')
    theme_button.pack()

def get_help_content():
    """Get comprehensive help content"""
    return """SymCalc - Professional Symbolic Calculator Help
================================================

GETTING STARTED:
• Enter mathematical expressions in the input field
• Press Enter or click "Calculate" to evaluate
• Use multi-line expressions with Shift+Enter
• Access functions via the Functions button

BASIC OPERATIONS:
+    Addition           -    Subtraction
*    Multiplication     /    Division
**   Power             ^    Alternative power
( )  Parentheses       =    Assignment

FUNCTIONS:
Trigonometric: sin(), cos(), tan(), asin(), acos(), atan()
Exponential:   exp(), log(), log10(), ln()
Roots:         sqrt(), cbrt()
Special:       gamma(), factorial(), beta(), erf()
Calculus:      diff(), integrate(), limit(), series()
Algebra:       solve(), expand(), factor(), simplify()

CONSTANTS:
pi   π (3.14159...)    e    Euler's number (2.718...)
oo   Infinity          I    Imaginary unit

VARIABLES:
x = 5                 Assign values to variables
y = x**2              Use variables in expressions
f(x) = x**2 + 2*x + 1 Define functions

COMPLEX NUMBERS:
1+2j, 3-4j           Complex number literals
re(z), im(z)         Real/imaginary parts
conjugate(z), abs(z) Complex operations

EXAMPLES:
Basic:        2 + 3 * 4 = 14
Trigonometry: sin(pi/2) = 1
Algebra:      solve(x**2 - 4, x) = [-2, 2]
Calculus:     diff(x**2, x) = 2*x
Integration:  integrate(x**2, x) = x**3/3
Variables:    x = 5; y = x**2; y = 25

KEYBOARD SHORTCUTS:
Enter          Calculate expression
Shift+Enter    New line in input
Ctrl+Enter     Calculate (alternative)
Ctrl+L         Clear input
Ctrl+H         Show history
F1             Show help
Ctrl+,         Show settings

POPUPS & FEATURES:
🧮 Calculator  Number keypad
🔧 Functions   Mathematical functions
📊 Variables   Current variables
📜 History     Calculation history
❓ Help         This help
⚙️ Settings    Theme and preferences

For more advanced features, see the CLI version with 'help' command.
"""
