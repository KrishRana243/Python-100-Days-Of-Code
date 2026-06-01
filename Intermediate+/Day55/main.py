# Higher or Lower URL

from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjN1Z3hkMjhwZ2lxeGV5b2k0ZG1hN3ZsbXNkMTlzdW9vZ2ZqMmFnZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LdzYJipCrdJqU/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXJhbnNpaWdsOWd2eHBncDd2enNmOHB2MnBjbnFyNXVhczNsZzBncyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XGBAmjqA0RJyU/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)