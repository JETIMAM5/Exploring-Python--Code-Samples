from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloworld():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://animalygifs.tumblr.com/post/25776406866" width="100%">')


def make_bold(func):
    def wrapper():
        return "<b>" + func() +"</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@make_bold
@make_emphasis
@make_underlined
@app.route('/bye')
def say_bye():
    return '<h3>Bye!</h3>'


@app.route("/username/<name>/<number>")
def greet(name, number):
    return f"Hello there {name}. You are {number} years old.!"


if __name__ == '__main__':
    # THis if statement allows us to run our code with 'run' button.
    # Auto - reloading the server with debug mode
    app.run(debug=True)