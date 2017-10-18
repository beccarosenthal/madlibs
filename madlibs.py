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


@app.route('/game')
def show_madlib_form():
    """Returns page in response to user decision re: the game"""
    play_game = request.args.get("game-dec")

    if play_game == "n":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """takes form for madlib from user, returns madlib text"""

    color = request.args.get("color").lower()
    person = request.args.get("person").title()
    noun = request.args.get("noun").lower()
    adjective = request.args.get("adj").lower()

    adj1 = request.args.get("adj1").lower()
    n1 = request.args.get("n1").lower()
    pv = request.args.get("pv").lower()
    adv1 = request.args.get("adv1").lower()
    adj2 = request.args.get("adj2").lower()
    n2 = request.args.get("n2").lower()
    n3 = request.args.get("n3").lower()
    adj3 = request.args.get("adj3").lower()
    v1 = request.args.get("v1").lower()
    adv2 = request.args.get("adv2").lower()
    pv2 = request.args.get("pv2").lower()
    adj4 = request.args.get("adj4").lower()

    return render_template("madlib.html", adjective1=adj1,
                            noun1=n1,
                            past_verb=pv,
                            adverb1=adv1,
                            adjective2=adj2,
                            noun2=n2,
                            noun3=n3,
                            adjective3=adj3
                            verb1=v1,
                            adverb2=adv2,
                            past_verb2=pv2,
                            adjective4=adj4)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)

