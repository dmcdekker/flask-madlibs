"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game_home')
def show_madlib_form():
    """Ask user if they want to paly the game."""

    get_answer = request.args.get("wants_game")
    get_item = request.args.get("item")
    print request.args

    if get_answer == 'True':
        return render_template("game.html", compliments=AWESOMENESS, item=get_item)
    elif get_answer == 'False':
        return render_template("goodbye.html")
    

    return render_template("madlib.html", wants_game=get_answer)

@app.route('/madlib')
def show_madlib():
    """Creates madlib style story"""

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    comp_type = request.args.get("comp_type")
    compliment = request.args.get("compliment")
    number = request.args.get("number")
    


    return render_template("madlib.html", person=person, color=color,
                                        noun=noun, number=number, compliment=compliment)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
