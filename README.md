# Python Calculator Project

Welcome to the **Python Calculator Project**! This is a straightforward yet fun calculator application that performs basic arithmetic operations: addition, subtraction, multiplication, and division. 

## 🎉 Overview

This calculator allows you to:
- Add, subtract, multiply, and divide numbers with ease.
- Continue calculations using the result of previous operations.
- Have a good laugh with a silly easter egg!

## 📄 Code Structure

Here's how the project is structured:

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

logo = """
 _____________________
|  _________________  |
| | Python   80085. | |  
| |_________________| | | 
|  ___ ___ ___   ___  | |
| | 7 | 8 | 9 | | + | | |
| |___|___|___| |___| | |
| | 4 | 5 | 6 | | - | | |
| |___|___|___| |___| | |
| | 1 | 2 | 3 | | x | | |
| |___|___|___| |___| | |
| | . | 0 | = | | / | | |
| |___|___|___| |___| | |
|_____________________|
"""
calculator = {"+": add, "-": subtract, "*": multiply, "/": divide}
```

## 🛠️ How to Run the Project

1. **Copy the Code**: Paste the code into a Python file named `calculator.py`.
2. **Run the Calculator**: Open your terminal or command prompt, navigate to the directory where the file is saved, and run:
   ```bash
   python calculator.py
   ```

## 🤪 Easter Egg Alert!

Feeling a bit adventurous? If at any point you want to escape the seemingly endless calculations, simply enter the mystical number **`8008569420`**! Voilà! You will be freed from the clutches of the while loop. 🎉 

It's like a secret code to unlock the exit door of this mathematical maze! Who knew calculators could be this fun?

## 🔍 Sample Output

Here's a sneak peek at what the calculator looks like in action:

```
 _____________________
|  _________________  |
| | Python   80085. | |  
| |_________________| | | 
|  ___ ___ ___   ___  | |
| | 7 | 8 | 9 | | + | | |
| |___|___|___| |___| | |
| | 4 | 5 | 6 | | - | | |
| |___|___|___| |___| | |
| | 1 | 2 | 3 | | x | | |
| |___|___|___| |___| | |
| | . | 0 | = | | / | | |
| |___|___|___| |___| | |
|_____________________|

What's the first number? 5
Pick an operation: +
What's the next number? 3
5.0 + 3.0 = 8.0
Type 'y' to continue calculating with 8.0, or type 'n' to start a new calculation: n

(And then it clears the screen)
```

## 💬 Join the Fun!

Feel free to add your own features, customize the logo, or even enhance the calculator's functionality! Have fun with it, and may your calculations always be accurate!

*Created with ❤️ by Somanath Nemilidinne*
