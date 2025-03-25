#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Your index() view should be routed to at the base URL with /. 
# It should Contain an h1 element that contains the title of this application, 
# "Python Operations with Flask Routing and Views".
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# A print_string view should take one parameter, a string.
# It should print the string in the console and display it in the web browser.
# Its URL should be of the format /print/parameter.
@app.route('/print/<string:mystring>')
def print_string(mystring):
    print(mystring)
    return mystring

# A count() view should take one parameter, an integer. 
# It should display all numbers in the range of that parameter on separate lines.
# Its URL should be of the format /count/parameter.
@app.route('/count/<int:par>')
def count(par):
    return "\n".join(str(e) for e in range(par)) + "\n"

# A math() view should take three parameters: num1, operation, and num2. 
# It must perform the appropriate operation on the two numbers in the order that they are presented. 
# The included operations should be: +, -, *, div (/ would change the URL path), and %. 
# Its URL should be of the format /math/<num1>/<operation>/<num2>.
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        myresult = num1 + num2
    elif operation == '-':
        myresult = num1 - num2
    elif operation == '*':
        myresult = num1 * num2
    elif operation == 'div':
        myresult = num1 / num2 if num2 != 0 else 'Undefined (division by zero)'
    elif operation == '%':
        myresult = num1 % num2
    else:
        return "Invalid operation"
    return str(myresult)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
