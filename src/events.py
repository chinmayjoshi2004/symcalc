import tkinter as tk
from utils import calculate, clear_input
from popups import show_history_popup, show_help_popup, show_settings_popup

def bind_events(gui_instance):
    """Bind keyboard and other events"""
    # Enter key for calculation
    gui_instance.input_entry.bind('<Return>', lambda e: gui_instance.calculate())
    gui_instance.input_entry.bind('<Shift-Return>', lambda e: gui_instance.insert_newline())
    gui_instance.root.bind('<Control-Return>', lambda e: gui_instance.calculate())

    # Keyboard shortcuts
    gui_instance.root.bind('<Control-l>', lambda e: gui_instance.clear_input())
    gui_instance.root.bind('<Control-h>', lambda e: gui_instance.show_history_popup())
    gui_instance.root.bind('<F1>', lambda e: gui_instance.show_help_popup())
    gui_instance.root.bind('<Control-comma>', lambda e: gui_instance.show_settings_popup())

    # Focus management
    gui_instance.input_entry.focus_set()

def on_input_change(gui_instance, event):
    current = gui_instance.input_entry.get()
    if current != gui_instance.current_input:
        gui_instance.undo_stack.append(gui_instance.current_input)
        gui_instance.current_input = current
    apply_syntax_highlighting(gui_instance)

def apply_syntax_highlighting(gui_instance):
    # Syntax highlighting is not supported for Entry widgets in Tkinter
    # This is a placeholder for future implementation with a Text widget
    pass

def undo_input(gui_instance):
    if gui_instance.undo_stack:
        gui_instance.input_entry.delete("1.0", tk.END)
        gui_instance.input_entry.insert("1.0", gui_instance.undo_stack.pop())

def insert_newline(gui_instance):
    gui_instance.input_entry.insert(tk.END, '\n')
