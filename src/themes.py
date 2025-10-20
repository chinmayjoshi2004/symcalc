import tkinter as tk
from tkinter import scrolledtext
import json
import os

def load_user_preferences():
    """Load user preferences from user.json"""
    try:
        with open('user.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'theme': 'dark',
            'precision': 4,
            'max_history': 100,
            'auto_save': True,
            'window_geometry': '1200x800+100+100'
        }

def save_user_preferences(preferences):
    """Save user preferences to user.json"""
    with open('user.json', 'w') as f:
        json.dump(preferences, f, indent=2)

def load_theme_preference():
    """Load theme preference from user preferences"""
    prefs = load_user_preferences()
    return prefs.get('theme', 'dark')

def save_theme_preference(current_theme):
    """Save theme preference to user preferences"""
    prefs = load_user_preferences()
    prefs['theme'] = current_theme
    save_user_preferences(prefs)

def toggle_theme(gui_instance):
    gui_instance.current_theme = 'dark' if gui_instance.current_theme == 'light' else 'light'
    apply_theme(gui_instance)
    save_theme_preference(gui_instance.current_theme)

def apply_theme(gui_instance):
    gui_instance.colors = gui_instance.themes.get(gui_instance.current_theme, gui_instance.themes['dark'])
    # Update root background
    gui_instance.root.configure(bg=gui_instance.colors['background'])

    # Update all widgets with new colors
    update_widget_colors(gui_instance.root, gui_instance.colors)

def update_widget_colors(widget, colors):
    # Update widget background and foreground based on type
    try:
        if isinstance(widget, tk.Frame):
            widget.configure(bg=colors['background'])
        elif isinstance(widget, tk.Label):
            widget.configure(bg=colors['background'], fg=colors['text'])
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=colors['surface'], fg=colors['text'], insertbackground=colors['text'])
        elif isinstance(widget, tk.Button):
            widget.configure(bg=colors['primary'], fg='white', activebackground=colors['secondary'])
        elif isinstance(widget, scrolledtext.ScrolledText):
            widget.configure(bg=colors['surface'], fg=colors['text'], insertbackground=colors['text'])
    except tk.TclError:
        # Some ttk widgets might not support direct color configuration
        pass

    # Recursively update children
    for child in widget.winfo_children():
        update_widget_colors(child, colors)
