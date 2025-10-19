# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-XX

### Added

- Initial release of SymCalc - Programmable Calculator
- Expression evaluation with SymPy backend
- Variable support for storing and reusing values
- Modern GUI with Tkinter
- Calculation history tracking
- Popup calculator interface with buttons
- Support for mathematical constants (pi, e)
- Built-in functions: sin, cos, tan, log, exp, sqrt, float
- Keyboard shortcuts (Enter to calculate)
- Help section with usage instructions
- Responsive design with modern color scheme

### Features

- Arithmetic operations: +, -, *, /, **
- Trigonometric functions
- Logarithmic and exponential functions
- Variable assignment and retrieval
- Formatted output (integers without decimals, 4-digit precision for floats)
- Smart history logging (only logs when result differs from input)

### Technical

- Python 3.6+ compatibility
- SymPy for symbolic mathematics
- Tkinter for GUI
- Modular architecture with separate evaluator and GUI classes
