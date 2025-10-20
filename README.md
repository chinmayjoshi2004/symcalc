# SymCalc - Programmable Calculator

A modern, feature-rich programmable calculator built with Python, Tkinter, and SymPy. Perform complex mathematical calculations, define variables, and use built-in functions with an intuitive graphical interface.

## Features

- **Expression Evaluation**: Evaluate mathematical expressions with support for variables, functions, and constants
- **Variable Support**: Define and reuse variables in calculations with persistent display
- **Advanced Functions**: Trigonometric, logarithmic, exponential, calculus (diff, integrate), algebraic (solve), and special functions (gamma, factorial)
- **Complex Numbers**: Support for complex number operations (1+2j, I for imaginary unit)
- **Modern GUI**: Clean, responsive interface with dark/light theme toggle and syntax highlighting
- **Calculation History**: Track your calculation history with smart logging
- **Keyboard Shortcuts**: Quick access with Enter, Ctrl+Z (undo), Ctrl+S (save history), and other shortcuts
- **Popup Calculator**: Enhanced button interface with function matrix layout
- **User Preferences**: Persistent settings stored in JSON format for themes and future customizations
- **Modular Architecture**: Well-organized codebase with separate modules for better maintainability

## Supported Operations

- Basic arithmetic: +, -, *, /, **
- Trigonometric functions: sin(), cos(), tan()
- Logarithmic functions: log()
- Exponential functions: exp()
- Square root: sqrt()
- Constants: pi, e
- Variable assignment: x = 5

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chinmayjoshi2004/symcalc.git
   cd symcalc
   ```

2. Install dependencies:

   ```bash
   pip install sympy
   ```

3. Run the application:

   ```bash
   python src/main.py
   ```

## Usage

1. Launch the application
2. Enter mathematical expressions in the input field
3. Press Enter or click "🚀 Calculate" to evaluate
4. Use the "➕ Add Buttons" popup for additional input options
5. View calculation history in the bottom panel

### Examples

- `2 + 3 * 4` → 14
- `sin(pi/2)` → 1
- `x = 10; x ** 2` → 100
- `sqrt(16) + log(100)` → 6
- `solve(x**2 - 4, x)` → [-2, 2]
- `diff(x**2, x)` → 2*x
- `integrate(x**2, x)` → x**3/3
- `gamma(5)` → 24
- `(1+2j) * (3-4j)` → (11+2j)

## Screenshots

![Calculator Interface](screenshots/main_interface.png)
![Button Popup](screenshots/button_popup.png)

## Requirements

- Python 3.6+
- Tkinter (usually included with Python)
- SymPy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Author

Created by [[chinmayjoshi2004](https://github.com/chinmayjoshi2004)]
