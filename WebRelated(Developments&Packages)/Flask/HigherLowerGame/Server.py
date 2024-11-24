from flask import Flask
from random import randint

LEAST = 1
MOST = 10
NUMBER_TO_GUESS = randint(LEAST, MOST)
START_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH =  "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW =  "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT =  "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
LINK_HTML = "<br>".join([f'<a href="/{num}">Guess number {num}</a>' for num in range(LEAST, MOST + 1)])

app = Flask(__name__)

def guess_decorator(function):
    def guess_wrapper():
        return function() + "<br>" + LINK_HTML
    return guess_wrapper

@app.route("/")
@guess_decorator
def guessing_game():
    return f'<h1>Try to guess a number between {LEAST} and {MOST}!</h1><br><img src= {START_GIF} alt="Centered Image" style="display: block; margin-left: auto; margin-right: auto;">'

def status_decorator(function):
    def status_wrapper(*args, **kwargs):
        return function(*args, **kwargs) + "<br>" + LINK_HTML
    return status_wrapper

@app.route('/<int:number>')
@status_decorator
def win_or_lose(number):
    if number > NUMBER_TO_GUESS:
        return (f'<h1 style="color:red; text-align: center">Too High! Try again!</h1><br>'
                f'<img src= {HIGH} alt="Centered Image" style="display: block; margin-left: auto; margin-right: auto;">><br>')
    elif number == NUMBER_TO_GUESS:
        return (f'<h1 style="color:green; text-align: center">You Found Me!</h1><br>'
                f'<img src= {CORRECT} alt="Centered Image" style="display: block; margin-left: auto; margin-right: auto;">>')
    else:
        return (f'<h1 style="color:Purple; text-align: center">Too Low! Try again!</h1><br>'
                f'<img src= {LOW} alt="Centered Image" style="display: block; margin-left: auto; margin-right: auto;">>')

if __name__ == "__main__":
    app.run(debug=True)
