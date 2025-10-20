# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-10-20

### Added

- **UI/UX Improvements**:
  - Dark/Light theme toggle with persistent user preferences
  - Syntax highlighting for input expressions (numbers, operators, functions)
  - Expanded keyboard shortcuts (Ctrl+Z for undo, Ctrl+S to save history)
- **Functionality Enhancements**:
  - Advanced math functions: gamma(), factorial(), complex numbers (1+2j)
  - Equation solving with solve() function
  - Symbolic manipulation: diff() for derivatives, integrate() for integrals
- **User Preferences System**:
  - Migrated from theme.txt to structured user.json file
  - Extensible preferences system for future settings
- **Modular Architecture**:
  - Refactored GUI into separate modules (config.py, themes.py, popups.py, layout.py, events.py, utils.py)
  - Improved code maintainability and separation of concerns

### Changed

- Enhanced calculator popup with additional function buttons (gamma, factorial, I)
- Improved variables display functionality in popup
- Updated help content to include new functions and features
- Better error handling and user feedback

### Fixed

- Variables popup now correctly displays in results area
- Theme persistence now uses JSON format instead of plain text
- Improved widget color updates during theme switching

## [1.1.0] - 2025-10-20

### Added

- Function matrix layout in popup (3x3 grid instead of vertical list)
- Smart welcome message clearing on first calculation
- Enhanced history management with proper state handling

### Changed

- Improved GUI responsiveness and user experience
- Updated documentation to reflect current features

### Fixed

- Welcome message now clears properly on first calculation
- History display updates correctly without duplication

## [1.0.0] - 2025-10-19

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
