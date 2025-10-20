# SymCalc - Programmable Calculator

[![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)

A modern, feature-rich programmable calculator built with Python, Tkinter, and SymPy. Perform complex mathematical calculations, define variables, and use built-in functions with an intuitive graphical interface. Designed for students, engineers, scientists, and anyone who needs powerful symbolic computation capabilities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Configuration](#configuration)
- [Screenshots](#screenshots)
- [Examples](#examples)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)
- [Author](#author)

## Features

### Core Functionality

- **Symbolic Mathematics**: Powered by SymPy for accurate symbolic computation
- **Expression Evaluation**: Support for complex mathematical expressions with proper operator precedence
- **Variable Management**: Define, store, and reuse variables across calculations
- **Function Library**: Extensive collection of mathematical functions (trigonometric, logarithmic, exponential, special functions)
- **Complex Numbers**: Full support for complex number operations and imaginary unit (I)
- **Equation Solving**: Solve algebraic equations symbolically
- **Calculus Operations**: Differentiation and integration capabilities
- **History Tracking**: Persistent calculation history with smart logging

### User Interface

- **Modern GUI**: Clean, responsive interface built with Tkinter
- **Theme Support**: Dark and light themes with persistent user preferences
- **Syntax Highlighting**: Color-coded input for better readability (numbers, operators, functions)
- **Enhanced Calculator Popup**: Organized button interface with tabbed layout:
  - **Numbers**: Standard numeric keypad with decimal and parentheses
  - **Operations**: Arithmetic operators (+, -, *, /, **, ^, //, %)
  - **Functions**: Mathematical functions (sin, cos, tan, log, exp, sqrt, etc.)
  - **Other**: Variables display and additional utilities
- **Responsive Design**: Adapts to different window sizes with resizable popup
- **Multi-line Input**: Support for complex multi-line expressions

### Advanced Features

- **Persistent Settings**: User preferences stored in JSON format
- **Keyboard Shortcuts**: Extensive shortcut support for power users
- **Undo/Redo**: Input editing with undo functionality
- **Smart Formatting**: Intelligent result formatting (integers, decimals, scientific notation)
- **Error Handling**: Comprehensive error messages and recovery
- **Modular Architecture**: Well-organized codebase for easy maintenance and extension

## Installation

### Prerequisites

- **Python 3.6 or higher**
- **Tkinter** (usually included with Python installations)
- **SymPy** (mathematical library)

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/chinmayjoshi2004/symcalc.git
   cd symcalc
   ```

2. **Create Virtual Environment (Recommended)**

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install sympy
   ```

4. **Verify Installation**

   ```bash
   python -c "import sympy; print('SymPy version:', sympy.__version__)"
   ```

5. **Run the Application**

   ```bash
   python main.py
   ```

### Alternative Installation Methods

**Using pip (if packaged):**

```bash
pip install symcalc
```

**Using conda:**

```bash
conda install sympy
python main.py
```

## Quick Start

1. Launch the application: `python main.py`
2. Enter a simple calculation: `2 + 3 * 4`
3. Press Enter or click "🚀 Calculate"
4. Try defining a variable: `x = 10`
5. Use the variable: `x ** 2`
6. Open the calculator popup: Click "➕ Add Buttons"
7. Explore different tabs: Numbers, Operations, Functions, Other

## Usage

### Basic Calculations

- Enter expressions directly in the input field
- Use standard mathematical notation
- Press Enter to calculate
- Results appear in the output area with history

### Variable Management

- Assign values: `x = 5`
- Use in expressions: `x * 2 + 3`
- View all variables: Click "📊 Variables" button or use popup

### Function Usage

- Built-in functions: `sin(pi/2)`, `sqrt(16)`, `log(100)`
- Function composition: `sin(cos(0))`
- Complex expressions: `exp(i*pi) + 1`

### Advanced Operations

- Equation solving: `solve(x**2 - 4, x)`
- Differentiation: `diff(x**2, x)`
- Integration: `integrate(x**2, x)`
- Symbolic manipulation: `expand((x+1)**2)`, `factor(x**2 - 1)`

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Calculate expression |
| `Shift + Enter` | New line in input |
| `Ctrl + Enter` | Calculate (alternative) |
| `Ctrl + L` | Clear input |
| `Ctrl + H` | Show history popup |
| `F1` | Show help |
| `Ctrl + ,` | Show settings |
| `Ctrl + Z` | Undo input |
| `Ctrl + S` | Save history |
| `Ctrl + Shift + S` | Save history to file |

## Configuration

### User Preferences

Settings are stored in `config/user.json`:

```json
{
  "theme": "dark",
  "window_size": {"width": 800, "height": 600},
  "font_size": 10,
  "history_limit": 100
}
```

### Theme Customization

Themes are defined in `config/themes.json`:

```json
{
  "dark": {
    "background": "#1e1e1e",
    "surface": "#2d2d2d",
    "text": "#ffffff",
    "primary": "#007acc",
    "accent": "#ff6b35"
  }
}
```

### Function Definitions

Custom functions can be added in `config/functions.json` for future extensibility.

## Screenshots

### Main Interface

![Main Calculator Interface](screenshots/main_interface.png)
*The main calculator interface showing input field, results area, and control buttons.*

### Calculator Popup

![Calculator Button Popup](screenshots/button_popup.png)
*Enhanced calculator popup with tabbed interface for Numbers, Operations, Functions, and Other.*

### Dark Theme

![Dark Theme Interface](screenshots/dark_theme.png)
*Calculator interface in dark theme with syntax highlighting.*

## Examples

### Basic Arithmetic

```txt
2 + 3 * 4 = 14
(10 - 3) / 2 = 3.5
2**3 + sqrt(16) = 12
```

### Trigonometric Functions

```txt
sin(pi/2) = 1
cos(0) = 1
tan(pi/4) = 1
```

### Variable Usage

```txt
x = 5
y = x**2 + 2*x + 1
y = 36
```

### Complex Numbers

```txt
z = 1 + 2*I
conjugate(z) = 1 - 2*I
abs(z) = sqrt(5)
```

### Equation Solving

```txt
solve(x**2 - 4, x) = [-2, 2]
solve(x**2 + 3*x - 10, x) = [-5, 2]
```

### Calculus

```txt
diff(x**2, x) = 2*x
integrate(x**2, x) = x**3/3
diff(sin(x), x) = cos(x)
```

### Advanced Functions

```txt
gamma(5) = 24
factorial(5) = 120
log10(100) = 2
exp(1) = e
```

## Architecture

### Project Structure

```txt
symcalc/
├── main.py                 # Application entry point
├── src/
│   ├── gui.py             # Main GUI class
│   ├── evaluator.py       # Expression evaluation logic
│   ├── config.py          # Configuration management
│   ├── themes.py          # Theme handling
│   ├── popups.py          # Popup windows (calculator, help, etc.)
│   ├── layout.py          # GUI layout setup
│   ├── events.py          # Event handling and shortcuts
│   └── utils.py           # Utility functions
├── config/
│   ├── config.json        # Application configuration
│   ├── themes.json        # Theme definitions
│   ├── functions.json     # Function definitions
│   ├── defaults.json      # Default settings
│   └── user.json          # User preferences
├── screenshots/           # Application screenshots
├── VERSION                # Version file
├── CHANGELOG.md           # Change history
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── LICENSE                # MIT License
```

### Key Components

- **GUI Layer**: Tkinter-based interface with modular components
- **Evaluation Engine**: SymPy-powered symbolic computation
- **Configuration System**: JSON-based settings management
- **Theme System**: Dynamic theming with persistence
- **Event System**: Keyboard shortcuts and user interactions

### Design Principles

- **Modularity**: Separate concerns into focused modules
- **Extensibility**: Easy to add new functions, themes, and features
- **User-Centric**: Intuitive interface with comprehensive help
- **Performance**: Efficient evaluation with smart caching
- **Maintainability**: Clean code with proper documentation

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Add tests if applicable
5. Commit your changes: `git commit -am 'Add some feature'`
6. Push to the branch: `git push origin feature/your-feature`
7. Submit a pull request

### Areas for Contribution

- New mathematical functions
- Additional themes
- UI/UX improvements
- Performance optimizations
- Documentation enhancements
- Bug fixes and testing

### Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable names
- Add docstrings to functions and classes
- Keep functions focused and modular

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and recent changes.

## Author

## **Chinmay Joshi**

- GitHub: [@chinmayjoshi2004](https://github.com/chinmayjoshi2004)
- Email: [chinmayjoshi4130@gmail.com](mailto:chinmayjoshi4130@gmail.com)

---

*SymCalc - Making symbolic mathematics accessible and powerful for everyone.*
