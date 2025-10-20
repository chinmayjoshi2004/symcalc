import tkinter as tk
from tkinter import filedialog

def show_welcome_message(gui_instance):
    """Display welcome message in results area"""
    welcome_text = """Welcome to SymCalc - Professional Symbolic Calculator!

Getting Started:
• Enter mathematical expressions in the input field above
• Press Enter or click "Calculate" to evaluate
• Use variables: x = 5, then y = x**2
• Access functions via the Functions button

Try these examples:
• 2 + 3 * 4
• sin(pi/2)
• solve(x**2 - 4, x)
• diff(x**2, x)
• integrate(x**2, x)

Type 'help' in the CLI version for more information.
"""
    gui_instance.results_display.insert(tk.END, welcome_text)
    gui_instance.results_display.config(state=tk.DISABLED)

def insert_text_to_entry(gui_instance, text):
    current = gui_instance.input_entry.get("1.0", tk.END)
    gui_instance.input_entry.delete("1.0", tk.END)
    gui_instance.input_entry.insert("1.0", current + text)

def clear_entry(gui_instance):
    gui_instance.input_entry.delete("1.0", tk.END)

def calculate_from_popup(gui_instance):
    calculate(gui_instance)

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
            gui_instance.results_display.insert(tk.END, f"> {expression}\n{formatted_result}\n\n")
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

def save_history(gui_instance):
    from tkinter import filedialog
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as f:
            f.write(gui_instance.history.get("1.0", tk.END))

def clear_input(gui_instance):
    gui_instance.input_entry.delete("1.0", tk.END)

def show_function_popup(gui_instance):
    popup = tk.Toplevel(gui_instance.root)
    popup.title("Functions")
    popup.geometry("400x400")
    popup.configure(bg=gui_instance.colors['background'])

    functions = ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'diff', 'integrate', 'solve', 'gamma', 'factorial']
    for i, func in enumerate(functions):
        row = i // 3
        col = i % 3
        btn = tk.Button(popup, text=func, command=lambda f=func: insert_text_to_entry(gui_instance, f + '('), bg=gui_instance.colors['surface'], fg=gui_instance.colors['text'], width=10, height=2)
        btn.grid(row=row, column=col, padx=5, pady=5)
