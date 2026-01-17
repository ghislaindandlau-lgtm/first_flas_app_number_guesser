from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        print("Before the function is called")
        result = f"<b>{func()}</b>"
        print("After the function is called")
        return result
    return wrapper

@app.route("/")
@make_bold
def hello_world():
    result = ("<h1>Guess a number between 0 and 9</h1>\n "
              "<image src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")
    return result

@app.route("/bye")
def buy_route():
    return "<b>bye world</b>"

