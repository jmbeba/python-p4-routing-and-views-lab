#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:print_str>')
def print_string(print_str):
    print(print_str)
    return print_str

@app.route('/count/<int:num>')
def count(num):
    return '\n'.join(str(n) for n in range(num)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'div':
        return str(num1 / num2)
    elif operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '%':
        return str(num1 % num2)
    
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
