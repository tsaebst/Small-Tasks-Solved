'''Create a new Python file called "calculator.py".
Define four functions in this file: add, subtract, multiply, and divide.
The add function should take two arguments and return their sum.
The subtract function should take two arguments and return their difference.
The multiply function should take two arguments and return their product.
The divide function should take two arguments and return their quotient.
Save the file.
Create a new Python file called "test_calculator.py".
Import the calculator module into this file.
Write test cases for each of the four functions, making sure to cover different input values and edge cases.
Run the test file and make sure all the tests pass.
Submit both files as your completed task.
Note: You can use any testing framework you like to write the test cases (e.g., unittest, pytest, etc.).'''

from calculator import *

def calculator():
    print("Welcome to Calculator.Demo! if you want to quit - enter 'Quit' on the next step.")
    while True:
        try:
            a = float(input("Input the first number:"))
            b = float(input("Input the second number:"))
        except:
            ask = input("The str obj has been inserted. Do you want to quit?").lower()
            if ask.startswith("y"):
                break
            print("Then try to enter the number, not the symbol.")
            continue
        ask = input("What do you want to do?(Add-A, Subtract - S, Multiply - M, Divide):").lower()
        if ask.startswith('a'):
            result = add(a, b)
        elif ask.startswith("d"):
            result = divide(a, b)
        elif ask.startswith("m"):
            result = multiply(a, b)
        elif ask.startswith("s"):
            result = subtract(a, b)
        elif ask.startswith("q"):
            break
        print("The result is:", result)
        print("Next attempt.")


calculator()