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


def add(a, b):
    result = a+b
    return result


def subtract(a, b):
    result = a-b
    return result


def divide(a, b):
    try:
        result = a/b
        return result
    except:
        print("Division on 0 is not available yet.")


def multiply(a, b):
    result = a*b
    return result