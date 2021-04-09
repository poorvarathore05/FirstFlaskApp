from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return """<h1>Welcome to my simple app</h1>
        <a href="/welcome">Go to welcome page</a>
    """


@app.route('/welcome')
def welcome_page():
    html = """
    <html>
      <body>
        <h1>Welcome</h1>
      </body>
    </html>
    """
    return html


@app.route('/welcome/home')
def wel_home():
    return """<h1>Welcome Home</h1>"""


@app.route('/welcome/back')
def wel_return():
    return """<h1>Welcome back</h1>"""
