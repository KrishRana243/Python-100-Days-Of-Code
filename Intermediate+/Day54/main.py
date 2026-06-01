from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/user/<name>")
def kanye(name):
    return f"Your name is {name} of mt. Olympus"

@app.route("/dev")
def gc():
    return "<h1>App Developer</h1>"

if __name__ == '__main__':
    app.run(debug = True)