# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/')
def diff_operations():
    return """<h1>Perform Different Operations</h1>"""


@app.route('/add')
def add_func():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a, b)
    return f"""<h2>Additon of numbers is {str(sum)}</h2>"""


@app.route('/subtract')
def sub_func():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    subtract = sub(a, b)
    return f"""<h2>Subtration of numbers is {str(subtract)}</h2>"""


@app.route('/multi')
def multi_func():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    multi = mult(a, b)
    return f"""<h2>Multiplication of numbers is {str(multi)}</h2>"""


@app.route('/divide')
def div_func():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    divide = div(a, b)
    return f"""<h2>Division of numbers is {str(divide)}</h2>"""
