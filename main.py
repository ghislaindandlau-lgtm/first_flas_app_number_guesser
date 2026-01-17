from flask import Flask
import random

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        print("Before the function is called")
        result = f"<b>{func()}</b>"
        print("After the function is called")
        return result
    return wrapper

RANDOM_NUMBER = random.randint(0,11)

@app.route("/")
@make_bold
def hello_world():
    result = ("<h1>Guess a number between 0 and 9</h1>\n "
              "<image src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")
    return result

@app.route("/<int:user_input>")
def evaluate_guess(user_input):
    if user_input == RANDOM_NUMBER:
        return "<image src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
    elif user_input < RANDOM_NUMBER:
        return "<image src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    elif user_input > RANDOM_NUMBER:
        return "<image src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"


@app.route("/bye")
def buy_route():
    return "<b>bye world</b>"

