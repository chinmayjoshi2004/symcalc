# src/gui.py
from .evaluator import CalculatorEvaluator

# Import modular components
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
import themes
import popups
import layout
import events
import utils

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.evaluator = CalculatorEvaluator()

        # Load configuration
        self.config = config.load_config()
        self.themes = config.load_themes()
        self.functions = config.load_functions()
        self.defaults = config.load_defaults()

        # Set window properties from config
        self.root.title(f"{self.config['app']['name']} - {self.config['app']['description']}")
        self.root.geometry(f"{self.config['ui']['window_size']['width']}x{self.config['ui']['window_size']['height']}")
        self.root.minsize(self.config['ui']['min_size']['width'], self.config['ui']['min_size']['height'])

        # Initialize state
        self.current_theme = themes.load_theme_preference()
        self.colors = self.themes.get(self.current_theme, self.themes['dark'])
        self.calculation_history = []
        self.current_expression = ""
        self.is_calculating = False
        self.undo_stack = []
        self.first_calculation = True

        layout.setup_styles(self)
        layout.create_layout(self)
        self.history = self.results_display  # Alias for backward compatibility
        events.bind_events(self)
        themes.apply_theme(self)

        # Welcome message
        utils.show_welcome_message(self)

    # Delegate methods to modular components
    def show_calculator_popup(self):
        popups.show_calculator_popup(self)

    def show_variables(self):
        popups.show_variables(self)

    def show_history_popup(self):
        popups.show_history_popup(self)

    def show_help_popup(self):
        popups.show_help_popup(self)

    def show_settings_popup(self):
        popups.show_settings_popup(self)

    def insert_text_to_entry(self, text):
        utils.insert_text_to_entry(self, text)

    def clear_entry(self):
        utils.clear_entry(self)

    def calculate_from_popup(self):
        utils.calculate_from_popup(self)

    def calculate(self):
        utils.calculate(self)

    def format_result(self, result):
        return utils.format_result(result)

    def load_theme_preference(self):
        return themes.load_theme_preference()

    def save_theme_preference(self):
        themes.save_theme_preference(self.current_theme)

    def toggle_theme(self):
        themes.toggle_theme(self)

    def apply_theme(self):
        themes.apply_theme(self)

    def update_widget_colors(self, widget):
        themes.update_widget_colors(widget, self.colors)

    def on_input_change(self, event):
        events.on_input_change(self, event)

    def apply_syntax_highlighting(self):
        events.apply_syntax_highlighting(self)

    def undo_input(self):
        events.undo_input(self)

    def save_history(self):
        utils.save_history(self)

    def clear_input(self):
        utils.clear_input(self)

    def show_function_popup(self):
        utils.show_function_popup(self)

    def insert_newline(self):
        events.insert_newline(self)

    def get_help_content(self):
        return popups.get_help_content()
