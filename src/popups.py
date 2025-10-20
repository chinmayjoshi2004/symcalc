import tkinter as tk
from tkinter import ttk, scrolledtext, Toplevel, messagebox

def show_calculator_popup(gui_instance):
    # Create a modern popup window for calculator buttons
    popup = Toplevel(gui_instance.root)
    popup.title("Calculator Buttons")
    popup.geometry("350x450")
    popup.configure(bg=gui_instance.colors['background'])
    popup.resizable(False, False)

    # Header
    header = tk.Label(popup,
                     text="🧮 Calculator Buttons",
                     font=("Segoe UI", 14, 'bold'),
                     bg=gui_instance.colors['primary'],
                     fg='white',
                     pady=10)
    header.pack(fill=tk.X)

    # Main content frame
    content_frame = tk.Frame(popup, bg=gui_instance.colors['background'], padx=15, pady=15)
    content_frame.pack(fill=tk.BOTH, expand=True)

    # Number buttons with modern styling
    numbers = [
        ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
        ('0', 3, 0), ('.', 3, 1), ('(', 3, 2), (')', 3, 3),
        ('+', 4, 3)
    ]

    for (text, row, col) in numbers:
        btn = tk.Button(content_frame,
                       text=text,
                       font=("Segoe UI", 12, 'bold'),
                       bg=gui_instance.colors['surface'],
                       fg=gui_instance.colors['text'],
                       activebackground=gui_instance.colors['primary'],
                       activeforeground='white',
                       relief='raised',
                       bd=2,
                       width=4,
                       height=2,
                       cursor='hand2',
                       command=lambda t=text: insert_text_to_entry(gui_instance, t))
        btn.grid(row=row, column=col, padx=3, pady=3)

    # Special buttons with modern styling
    clear_btn = tk.Button(content_frame,
                         text='🗑️ C',
                         font=("Segoe UI", 11, 'bold'),
                         bg='#dc3545',
                         fg='white',
                         activebackground='#c82333',
                         activeforeground='white',
                         relief='raised',
                         bd=2,
                         width=8,
                         height=2,
                         cursor='hand2',
                         command=lambda: clear_entry(gui_instance))
    clear_btn.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

    calc_btn = tk.Button(content_frame,
                        text='✅ =',
                        font=("Segoe UI", 11, 'bold'),
                        bg=gui_instance.colors['accent'],
                        fg='white',
                        activebackground='#e55a2b',
                        activeforeground='white',
                        relief='raised',
                        bd=2,
                        width=8,
                        height=2,
                        cursor='hand2',
                        command=lambda: [calculate_from_popup(gui_instance), popup.destroy()])
    calc_btn.grid(row=4, column=2, columnspan=2, padx=3, pady=3)

    # Function buttons section
    func_label = tk.Label(content_frame,
                         text="Functions:",
                         font=("Segoe UI", 10, 'bold'),
                         bg=gui_instance.colors['background'],
                         fg=gui_instance.colors['text'])
    func_label.grid(row=5, column=0, columnspan=4, pady=(15, 5), sticky=tk.W)

    functions = ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'float', 'pi', 'e', 'gamma', 'factorial', 'I']
    for i, func in enumerate(functions):
        btn = tk.Button(content_frame,
                       text=func,
                       font=("Segoe UI", 9),
                       bg=gui_instance.colors['surface'],
                       fg=gui_instance.colors['text'],
                       activebackground=gui_instance.colors['primary'],
                       activeforeground='white',
                       relief='raised',
                       bd=1,
                       width=6,
                       height=1,
                       cursor='hand2',
                       command=lambda f=func: insert_text_to_entry(gui_instance, f + '('))
        btn.grid(row=6 + i//4, column=i%4, padx=2, pady=2)

    # Variables button
    vars_btn = tk.Button(content_frame,
                        text='📊 Vars',
                        font=("Segoe UI", 10, 'bold'),
                        bg=gui_instance.colors['secondary'],
                        fg='white',
                        activebackground=gui_instance.colors['primary'],
                        activeforeground='white',
                        relief='raised',
                        bd=2,
                        width=12,
                        height=2,
                        cursor='hand2',
                        command=lambda: show_variables(gui_instance))
    vars_btn.grid(row=8, column=0, columnspan=4, pady=(10, 0))

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
