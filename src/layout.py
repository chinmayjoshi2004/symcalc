import tkinter as tk
from tkinter import ttk, scrolledtext
from utils import calculate, clear_input, show_function_popup
from popups import show_calculator_popup, show_variables, show_history_popup, show_help_popup, show_settings_popup
from themes import toggle_theme

def setup_styles(gui_instance):
    """Configure ttk styles for professional appearance"""
    gui_instance.style = ttk.Style()

    # Configure main styles
    gui_instance.style.configure('Card.TFrame',
                               background=gui_instance.colors['surface'],
                               relief='raised',
                               borderwidth=1)

    gui_instance.style.configure('Header.TLabel',
                               font=('Segoe UI', 16, 'bold'),
                               background=gui_instance.colors['surface'],
                               foreground=gui_instance.colors['text'])

    gui_instance.style.configure('Subheader.TLabel',
                               font=('Segoe UI', 12, 'bold'),
                               background=gui_instance.colors['surface'],
                               foreground=gui_instance.colors['text_secondary'])

    gui_instance.style.configure('Primary.TButton',
                               font=('Segoe UI', 10, 'bold'),
                               padding=(20, 10),
                               relief='flat',
                               background=gui_instance.colors['primary'],
                               foreground='white')

    gui_instance.style.configure('Secondary.TButton',
                               font=('Segoe UI', 9),
                               padding=(15, 8),
                               relief='flat')

    gui_instance.style.configure('Accent.TButton',
                               font=('Segoe UI', 10, 'bold'),
                               padding=(20, 10),
                               relief='flat',
                               background=gui_instance.colors['accent'],
                               foreground='white')

def create_layout(gui_instance):
    """Create the main application layout"""
    # Main container
    main_container = tk.Frame(gui_instance.root, bg=gui_instance.colors['background'])
    main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Configure grid weights
    gui_instance.root.columnconfigure(0, weight=1)
    gui_instance.root.rowconfigure(0, weight=1)
    main_container.columnconfigure(1, weight=1)
    main_container.rowconfigure(1, weight=1)

    # Sidebar (left panel)
    create_sidebar(gui_instance, main_container)

    # Main content area (right panel)
    create_main_content(gui_instance, main_container)

    # Status bar
    create_status_bar(gui_instance, main_container)

def create_sidebar(gui_instance, parent):
    """Create the sidebar with quick access buttons"""
    sidebar = tk.Frame(parent, bg=gui_instance.colors['surface_secondary'],
                      width=250, relief='solid', bd=1)
    sidebar.grid(row=0, column=0, rowspan=2, sticky=(tk.W, tk.N, tk.S), padx=(0, 10), pady=10)
    sidebar.grid_propagate(False)

    # Sidebar header
    sidebar_header = tk.Label(sidebar, text="Quick Access",
                            font=('Segoe UI', 14, 'bold'),
                            bg=gui_instance.colors['surface_secondary'],
                            fg=gui_instance.colors['text'])
    sidebar_header.pack(pady=(20, 15), padx=15, anchor='w')

    # Quick action buttons
    actions = [
        ("🧮 Calculator", lambda: show_calculator_popup(gui_instance)),
        ("📊 Variables", lambda: show_variables(gui_instance)),
        ("📜 History", lambda: show_history_popup(gui_instance)),
        ("❓ Help", lambda: show_help_popup(gui_instance)),
        ("⚙️ Settings", lambda: show_settings_popup(gui_instance))
    ]

    for text, command in actions:
        btn = tk.Button(sidebar, text=text,
                      font=('Segoe UI', 10),
                      bg=gui_instance.colors['surface'],
                      fg=gui_instance.colors['text'],
                      activebackground=gui_instance.colors['primary'],
                      activeforeground='white',
                      relief='flat', bd=0,
                      padx=15, pady=10,
                      cursor='hand2',
                      command=command)
        btn.pack(fill=tk.X, padx=10, pady=(0, 5))

    # Theme toggle
    theme_frame = tk.Frame(sidebar, bg=gui_instance.colors['surface_secondary'])
    theme_frame.pack(fill=tk.X, padx=10, pady=(20, 10))

    theme_label = tk.Label(theme_frame, text="Theme:",
                         font=('Segoe UI', 10),
                         bg=gui_instance.colors['surface_secondary'],
                         fg=gui_instance.colors['text_secondary'])
    theme_label.pack(anchor='w')

    gui_instance.theme_toggle = tk.Button(theme_frame,
                                        text="🌙 Dark" if gui_instance.current_theme == 'light' else "☀️ Light",
                                        font=('Segoe UI', 9, 'bold'),
                                        bg=gui_instance.colors['primary'],
                                        fg='white',
                                        activebackground=gui_instance.colors['secondary'],
                                        relief='flat', bd=0,
                                        padx=10, pady=5,
                                        cursor='hand2',
                                        command=lambda: toggle_theme(gui_instance))
    gui_instance.theme_toggle.pack(anchor='w', pady=(5, 0))

def create_main_content(gui_instance, parent):
    """Create the main content area with input and results"""
    content_frame = tk.Frame(parent, bg=gui_instance.colors['background'])
    content_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
    content_frame.columnconfigure(0, weight=1)
    content_frame.rowconfigure(1, weight=1)

    # Input section
    input_card = tk.Frame(content_frame, bg=gui_instance.colors['surface'],
                        relief='solid', bd=1)
    input_card.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
    input_card.columnconfigure(0, weight=1)

    # Input header
    input_header = tk.Label(input_card, text="Expression Input",
                          font=('Segoe UI', 14, 'bold'),
                          bg=gui_instance.colors['surface'],
                          fg=gui_instance.colors['text'])
    input_header.grid(row=0, column=0, sticky=tk.W, padx=20, pady=(20, 10))

    # Input field with modern styling
    gui_instance.input_entry = tk.Text(input_card,
                                     height=3,
                                     font=('Consolas', 12),
                                     bg=gui_instance.colors['surface_secondary'],
                                     fg=gui_instance.colors['text'],
                                     insertbackground=gui_instance.colors['text'],
                                     relief='flat',
                                     bd=2,
                                     padx=15, pady=10,
                                     wrap=tk.WORD)
    gui_instance.input_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=20, pady=(0, 15))

    # Action buttons
    button_frame = tk.Frame(input_card, bg=gui_instance.colors['surface'])
    button_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=20, pady=(0, 20))

    # Calculate button
    calc_btn = tk.Button(button_frame, text="⚡ Calculate",
                       font=('Segoe UI', 11, 'bold'),
                       bg=gui_instance.colors['accent'],
                       fg='white',
                       activebackground=gui_instance.colors['warning'],
                       relief='flat', bd=0,
                       padx=25, pady=12,
                       cursor='hand2',
                       command=lambda: calculate(gui_instance))
    calc_btn.pack(side=tk.LEFT, padx=(0, 15))

    # Clear button
    clear_btn = tk.Button(button_frame, text="🗑️ Clear",
                        font=('Segoe UI', 10),
                        bg=gui_instance.colors['error'],
                        fg='white',
                        activebackground='#dc2626',
                        relief='flat', bd=0,
                        padx=20, pady=10,
                        cursor='hand2',
                        command=lambda: clear_input(gui_instance))
    clear_btn.pack(side=tk.LEFT, padx=(0, 15))

    # Function buttons
    func_btn = tk.Button(button_frame, text="🔧 Functions",
                       font=('Segoe UI', 10),
                       bg=gui_instance.colors['primary'],
                       fg='white',
                       activebackground=gui_instance.colors['secondary'],
                       relief='flat', bd=0,
                       padx=20, pady=10,
                       cursor='hand2',
                       command=lambda: show_function_popup(gui_instance))
    func_btn.pack(side=tk.LEFT)

    # Results section
    results_card = tk.Frame(content_frame, bg=gui_instance.colors['surface'],
                          relief='solid', bd=1)
    results_card.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    results_card.columnconfigure(0, weight=1)
    results_card.rowconfigure(1, weight=1)

    # Results header
    results_header = tk.Label(results_card, text="Results & History",
                            font=('Segoe UI', 14, 'bold'),
                            bg=gui_instance.colors['surface'],
                            fg=gui_instance.colors['text'])
    results_header.grid(row=0, column=0, sticky=tk.W, padx=20, pady=(20, 10))

    # Results display
    gui_instance.results_display = scrolledtext.ScrolledText(
        results_card,
        height=15,
        font=('Consolas', 10),
        bg=gui_instance.colors['surface_secondary'],
        fg=gui_instance.colors['text'],
        insertbackground=gui_instance.colors['text'],
        relief='flat',
        bd=0,
        padx=15, pady=10
    )
    gui_instance.results_display.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S),
                                    padx=20, pady=(0, 20))

def create_status_bar(gui_instance, parent):
    """Create the status bar at the bottom"""
    status_frame = tk.Frame(parent, bg=gui_instance.colors['surface_secondary'],
                          height=30, relief='solid', bd=1)
    status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    status_frame.grid_propagate(False)

    gui_instance.status_label = tk.Label(status_frame,
                                       text="Ready",
                                       font=('Segoe UI', 9),
                                       bg=gui_instance.colors['surface_secondary'],
                                       fg=gui_instance.colors['text_secondary'])
    gui_instance.status_label.pack(side=tk.LEFT, padx=15)

    # Version info
    version_label = tk.Label(status_frame,
                           text=f"{gui_instance.config['app']['name']} v{gui_instance.config['app']['version']}",
                           font=('Segoe UI', 9),
                           bg=gui_instance.colors['surface_secondary'],
                           fg=gui_instance.colors['text_muted'])
    version_label.pack(side=tk.RIGHT, padx=15)
