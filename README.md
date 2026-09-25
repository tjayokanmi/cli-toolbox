# CLI Toolbox

A beginner-friendly Python command-line application that combines several small utilities into one interactive toolbox.

This project was built as part of my Python learning journey to practice **functions, conditionals, loops, input validation, exception handling, modules, and basic project organization**.

## Features

### 1. Unit Converter

Supports:

- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Kilometers → Miles
- Miles → Kilometers

### 2. Calculator

Supports:

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero handling

### 3. Number Guessing Game

- Generates a random number between 1 and 20
- Gives the player 6 attempts
- Provides higher/lower hints
- Handles invalid numeric input

## Project Structure

```text
CLI Toolbox/
├── main.py
├── calculator.py
├── unit_converter.py
├── guessing_game.py
└── utils.py
```

### File Overview

- `main.py` — Main menu and application entry point
- `calculator.py` — Calculator operations and menu
- `unit_converter.py` — Unit conversion functions and menu
- `guessing_game.py` — Number guessing game
- `utils.py` — Shared input-validation utility

## Concepts Practiced

This project helped me practice:

- Variables and data types
- Functions and parameters
- Return values
- `if / elif / else`
- `for` and `while` loops
- `break`
- `try / except`
- `ValueError`
- `ZeroDivisionError`
- User input
- Random number generation
- Python modules and imports
- Code reuse
- Basic separation of responsibilities

## How to Run

Make sure Python 3 is installed.

Clone or download the project, then run:

```bash
python main.py
```

Follow the menu prompts to select a tool.

## What I Learned

The main lesson from this project was that good code is not simply about making a program work. It is also about understanding **how to break a problem into smaller responsibilities**.

I practiced separating user interaction from reusable functions and learned when simple repetition is acceptable instead of creating unnecessary abstractions.

## Status

**Completed — Python Phase 1 learning project.**

This project is intentionally kept simple as a learning exercise.
