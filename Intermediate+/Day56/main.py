import requests

# The code below will not work for the live website because the HTML has changed.

response = requests.get("https://angelabauer.github.io/cv/")

cv = response.text
#print(cv)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("cv.html")

@app.route('/1')
def programmer():
    return render_template("angela.html")

@app.route('/2')
def index():
    return render_template("index.html")

@app.route('/3')
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)