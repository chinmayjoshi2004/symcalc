import tkinter as tk
from tkinter import ttk, scrolledtext, Toplevel
from evaluator import CalculatorEvaluator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Programmable Calculator")
        self.root.geometry("900x600")
        self.root.state('normal')  # Ensure window is not maximized
        self.root.configure(bg='#f0f0f0')
        self.evaluator = CalculatorEvaluator()

        # Define modern color scheme
        self.colors = {
            'primary': '#007acc',
            'secondary': '#005a9e',
            'accent': '#ff6b35',
            'background': '#f8f9fa',
            'surface': '#ffffff',
            'text': '#212529',
            'text_secondary': '#6c757d',
            'border': '#dee2e6'
        }

        # Set modern style
        style = ttk.Style()
        style.configure('TFrame', background=self.colors['background'])
        style.configure('TButton',
                       font=('Segoe UI', 10, 'bold'),
                       padding=8,
                       relief='flat',
                       background=self.colors['primary'],
                       foreground='white')
        style.map('TButton',
                 background=[('active', self.colors['secondary'])])
        style.configure('TLabel',
                       font=('Segoe UI', 11),
                       background=self.colors['background'],
                       foreground=self.colors['text'])
        style.configure('TEntry',
                       font=('Consolas', 12),
                       padding=8,
                       relief='flat')

        # Create main frame with vertical layout
        main_frame = ttk.Frame(root, padding="20", style='TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Top section: Input area
        input_frame = ttk.Frame(main_frame, style='TFrame')
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))

        # Input label
        input_label = tk.Label(input_frame,
                              text="🔢 Expression Input",
                              font=("Segoe UI", 12, 'bold'),
                              bg=self.colors['background'],
                              fg=self.colors['text'])
        input_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))

        # Modern input entry with rounded corners effect
        self.input_entry = tk.Entry(input_frame,
                                   font=("Consolas", 16, 'bold'),
                                   bg=self.colors['surface'],
                                   fg=self.colors['text'],
                                   insertbackground=self.colors['text'],
                                   relief='flat',
                                   bd=2,
                                   highlightthickness=2,
                                   highlightbackground=self.colors['border'],
                                   highlightcolor=self.colors['primary'])
        self.input_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))

        # Button row
        button_frame = tk.Frame(input_frame, bg=self.colors['background'])
        button_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

        # Modern buttons with hover effects
        add_btn = tk.Button(button_frame,
                           text="➕ Add Buttons",
                           font=("Segoe UI", 11, 'bold'),
                           bg=self.colors['primary'],
                           fg='white',
                           activebackground=self.colors['secondary'],
                           activeforeground='white',
                           relief='flat',
                           bd=0,
                           padx=25,
                           pady=10,
                           cursor='hand2',
                           command=self.show_button_popup)
        add_btn.pack(side=tk.LEFT, padx=(0, 15))

        send_btn = tk.Button(button_frame,
                            text="🚀 Calculate",
                            font=("Segoe UI", 11, 'bold'),
                            bg=self.colors['accent'],
                            fg='white',
                            activebackground='#e55a2b',
                            activeforeground='white',
                            relief='flat',
                            bd=0,
                            padx=25,
                            pady=10,
                            cursor='hand2',
                            command=self.calculate)
        send_btn.pack(side=tk.LEFT)

        input_frame.columnconfigure(0, weight=1)

        # Bottom section: History and Help stacked vertically
        content_frame = ttk.Frame(main_frame, style='TFrame')
        content_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # History section
        history_frame = tk.Frame(content_frame, bg=self.colors['surface'], bd=2, relief='solid')
        history_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 15))

        history_label = tk.Label(history_frame,
                                text="📜 Calculation History",
                                font=("Segoe UI", 13, 'bold'),
                                bg=self.colors['surface'],
                                fg=self.colors['text'])
        history_label.grid(row=0, column=0, sticky=tk.W, padx=15, pady=(15, 10))

        self.history = scrolledtext.ScrolledText(history_frame,
                                               height=10,
                                               width=80,
                                               wrap=tk.WORD,
                                               font=("Consolas", 10),
                                               bg=self.colors['surface'],
                                               fg=self.colors['text'],
                                               insertbackground=self.colors['text'],
                                               relief='flat',
                                               bd=0,
                                               padx=15,
                                               pady=5)
        self.history.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=15, pady=(0, 15))

        # Help section
        help_frame = tk.Frame(content_frame, bg=self.colors['surface'], bd=2, relief='solid')
        help_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        help_label = tk.Label(help_frame,
                             text="❓ Help & Keyboard Shortcuts",
                             font=("Segoe UI", 13, 'bold'),
                             bg=self.colors['surface'],
                             fg=self.colors['text'])
        help_label.grid(row=0, column=0, sticky=tk.W, padx=15, pady=(15, 10))

        self.help_text = scrolledtext.ScrolledText(help_frame,
                                                 height=10,
                                                 width=80,
                                                 wrap=tk.WORD,
                                                 font=("Segoe UI", 9),
                                                 bg=self.colors['surface'],
                                                 fg=self.colors['text_secondary'],
                                                 relief='flat',
                                                 bd=0,
                                                 padx=15,
                                                 pady=5)
        self.help_text.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=15, pady=(0, 15))
        self.help_text.insert(tk.END, self.get_help_text())
        self.help_text.config(state=tk.DISABLED)

        # Bind Enter key to calculate function
        self.input_entry.bind('<Return>', lambda event: self.calculate())
        self.root.bind('<Return>', lambda event: self.calculate())

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(0, weight=1)
        content_frame.rowconfigure(1, weight=1)
        history_frame.columnconfigure(0, weight=1)
        help_frame.columnconfigure(0, weight=1)

    def show_button_popup(self):
        # Create a modern popup window for calculator buttons
        popup = Toplevel(self.root)
        popup.title("Calculator Buttons")
        popup.geometry("350x450")
        popup.configure(bg=self.colors['background'])
        popup.resizable(False, False)

        # Header
        header = tk.Label(popup,
                         text="🧮 Calculator Buttons",
                         font=("Segoe UI", 14, 'bold'),
                         bg=self.colors['primary'],
                         fg='white',
                         pady=10)
        header.pack(fill=tk.X)

        # Main content frame
        content_frame = tk.Frame(popup, bg=self.colors['background'], padx=15, pady=15)
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
                           bg=self.colors['surface'],
                           fg=self.colors['text'],
                           activebackground=self.colors['primary'],
                           activeforeground='white',
                           relief='raised',
                           bd=2,
                           width=4,
                           height=2,
                           cursor='hand2',
                           command=lambda t=text: self.insert_text_to_entry(t))
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
                             command=self.clear_entry)
        clear_btn.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

        calc_btn = tk.Button(content_frame,
                            text='✅ =',
                            font=("Segoe UI", 11, 'bold'),
                            bg=self.colors['accent'],
                            fg='white',
                            activebackground='#e55a2b',
                            activeforeground='white',
                            relief='raised',
                            bd=2,
                            width=8,
                            height=2,
                            cursor='hand2',
                            command=lambda: [self.calculate_from_popup(), popup.destroy()])
        calc_btn.grid(row=4, column=2, columnspan=2, padx=3, pady=3)

        # Function buttons section
        func_label = tk.Label(content_frame,
                             text="Functions:",
                             font=("Segoe UI", 10, 'bold'),
                             bg=self.colors['background'],
                             fg=self.colors['text'])
        func_label.grid(row=5, column=0, columnspan=4, pady=(15, 5), sticky=tk.W)

        functions = ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'float', 'pi', 'e']
        for i, func in enumerate(functions):
            btn = tk.Button(content_frame,
                           text=func,
                           font=("Segoe UI", 9),
                           bg=self.colors['surface'],
                           fg=self.colors['text'],
                           activebackground=self.colors['primary'],
                           activeforeground='white',
                           relief='raised',
                           bd=1,
                           width=6,
                           height=1,
                           cursor='hand2',
                           command=lambda f=func: self.insert_text_to_entry(f + '('))
            btn.grid(row=6 + i//4, column=i%4, padx=2, pady=2)

        # Variables button
        vars_btn = tk.Button(content_frame,
                            text='📊 Vars',
                            font=("Segoe UI", 10, 'bold'),
                            bg=self.colors['secondary'],
                            fg='white',
                            activebackground=self.colors['primary'],
                            activeforeground='white',
                            relief='raised',
                            bd=2,
                            width=12,
                            height=2,
                            cursor='hand2',
                            command=self.show_variables)
        vars_btn.grid(row=8, column=0, columnspan=4, pady=(10, 0))

    def insert_text_to_entry(self, text):
        current = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, current + text)

    def clear_entry(self):
        self.input_entry.delete(0, tk.END)

    def calculate_from_popup(self):
        self.calculate()

    def calculate(self):
        expression = self.input_entry.get().strip()
        if expression:
            result = self.evaluator.evaluate(expression)
            formatted_result = self.format_result(result)
            # Only add to history if the result differs from the input expression
            if formatted_result != expression:
                self.history.insert(tk.END, f"> {expression}\n{formatted_result}\n\n")
                self.history.see(tk.END)
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, formatted_result)

    def format_result(self, result):
        try:
            num = float(result)
            if num.is_integer():
                return str(int(num))
            else:
                return f"{num:.4f}".rstrip('0').rstrip('.')
        except ValueError:
            return str(result)

    def show_variables(self):
        vars_str = self.evaluator.get_variables()
        self.history.insert(tk.END, f"Variables:\n{vars_str}\n\n")
        self.history.see(tk.END)

    def get_help_text(self):
        return """Keyboard Shortcuts:
Enter - Calculate expression
Ctrl+C - Clear input
Ctrl+V - Paste

Supported Operations:
+ Addition
- Subtraction
* Multiplication
/ Division
** Power
sin(), cos(), tan() - Trigonometric functions
log() - Natural logarithm
exp() - Exponential
sqrt() - Square root
pi, e - Constants

Variable Assignment:
x = 5
y = x + 3

Examples:
2 + 3 * 4
sin(pi/2)
x = 10
x ** 2"""
