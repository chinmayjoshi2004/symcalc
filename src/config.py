import json

def load_config():
    """Load application configuration from config.json"""
    try:
        with open('config/config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            # Extract the relevant parts for the GUI
            return {
                'app': config.get('app', {
                    'name': 'SymCalc',
                    'description': 'Professional Symbolic Calculator',
                    'version': '1.0'
                }),
                'ui': config.get('ui', {
                    'window_size': {'width': 1200, 'height': 800},
                    'min_size': {'width': 1000, 'height': 700}
                })
            }
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'app': {
                'name': 'SymCalc',
                'description': 'Professional Symbolic Calculator',
                'version': '1.0'
            },
            'ui': {
                'window_size': {'width': 1200, 'height': 800},
                'min_size': {'width': 1000, 'height': 700}
            }
        }

def load_themes():
    """Load theme configurations from themes.json"""
    try:
        with open('config/themes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'light': {
                'primary': '#2563eb',
                'secondary': '#1d4ed8',
                'accent': '#f59e0b',
                'success': '#10b981',
                'error': '#ef4444',
                'warning': '#f59e0b',
                'background': '#ffffff',
                'surface': '#f8fafc',
                'surface_secondary': '#f1f5f9',
                'text': '#1e293b',
                'text_secondary': '#64748b',
                'text_muted': '#94a3b8',
                'border': '#e2e8f0',
                'border_light': '#f1f5f9',
                'shadow': '#00000010'
            },
            'dark': {
                'primary': '#3b82f6',
                'secondary': '#1d4ed8',
                'accent': '#fbbf24',
                'success': '#34d399',
                'error': '#f87171',
                'warning': '#fbbf24',
                'background': '#0f172a',
                'surface': '#1e293b',
                'surface_secondary': '#334155',
                'text': '#f8fafc',
                'text_secondary': '#cbd5e1',
                'text_muted': '#64748b',
                'border': '#334155',
                'border_light': '#475569',
                'shadow': '#00000040'
            }
        }

def load_functions():
    """Load function configurations from functions.json"""
    try:
        with open('config/functions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'trigonometric': ['sin', 'cos', 'tan', 'asin', 'acos', 'atan'],
            'exponential': ['exp', 'log', 'log10', 'ln'],
            'roots': ['sqrt', 'cbrt'],
            'special': ['gamma', 'factorial', 'beta', 'erf'],
            'calculus': ['diff', 'integrate', 'limit', 'series'],
            'algebra': ['solve', 'expand', 'factor', 'simplify']
        }

def load_defaults():
    """Load default settings from defaults.json"""
    try:
        with open('config/defaults.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'theme': 'dark',
            'precision': 4,
            'max_history': 100,
            'auto_save': True
        }
