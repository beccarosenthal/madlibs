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

DISSES = [
    "scurvey companion", "pigeon-liver'd hobby horse", "poisonous bunch-backed toad",
    "stewed prune", "bolting hutch of beastliness", "swollen parcel of dropsies",
    "huge bombard of sack", "stuffed cloak bag of guts", "plague sore"]

HOW_COOL = ["somewhat cool", "super cool", "not that cool",
            "cool enough for the circumstances", "uncool", "cool"]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    #right now, input list sends to jinja as a string, not as html. Change that. 

    input_list = ""
    for coolness in HOW_COOL:
        input_list = input_list + ('<input type="checkbox" name="coolness" value="{}">{}'
                                   .format(coolness, coolness.title()))
    
    return render_template("hello.html", input_list=input_list)


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")
    coolness = request.args.getlist("coolness")

    ###Trying to print out coolness in list with oxford comma
    if coolness:
        cool_string = coolness[0]

        if len(coolness) == 2:
            cool_string = cool_string + " and " + coolness[1]
        elif len(coolness) > 2:
            for item in coolness[1:-1]:
                cool_string = cool_string + ", " + item
            cool_string = cool_string + ", and " + coolness[-1]
    else:
        cool_string = "You're not cool enough to gague your coolness. Loser."

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment,
                           coolness=cool_string)


@app.route('/game')
def show_madlib_form():
    """Returns page in response to user decision re: the game"""

    play_game = request.args.get("game-dec")

    pairs = {
        'adjective1': ["adj1"],
        'noun1': ["n1"],
        'past_verb1': ["pv"],
        'adverb1': ["adv1"],
        'adjective2': ["adj2"],
        'noun2': ["n2"],
        'noun3': ["n3"],
        'adjective3': ["adj3"],
        'verb1': ["v1"],
        'verb2': ["verb2"],
        'past_verb2': ["pv2"],
        'adjective4': ["adj4"]
        }
     #append the display version of the key to list at value
    for key in pairs:
        pairs[key].append(key[:-1].replace("_", " ").title())

    if play_game == "n":
        insult = choice(DISSES)
        return render_template("goodbye.html", insult=insult)
    else:
        return render_template("game.html", pairs=pairs)


@app.route('/madlib')
def show_madlib():
    """takes form for madlib from user, returns madlib text"""

    # color = request.args.get("color").lower()
    # person = request.args.get("person").title()
    # noun = request.args.get("noun").lower()
    # adjective = request.args.get("adj").lower()

    adj1 = request.args.get("adj1").lower()
    n1 = request.args.get("n1").lower()
    pv = request.args.get("pv").lower()
    adv1 = request.args.get("adv1").lower()
    adj2 = request.args.get("adj2").lower()
    n2 = request.args.get("n2").lower()
    n3 = request.args.get("n3").lower()
    adj3 = request.args.get("adj3").lower()
    v1 = request.args.get("v1").lower()
    verb2 = request.args.get("verb2").lower()
    pv2 = request.args.get("pv2").lower()
    adj4 = request.args.get("adj4").lower()



    return render_template("madlib.html",  
                            adjective1=adj1,
                            noun1=n1,
                            past_verb1=pv,
                            adverb1=adv1,
                            adjective2=adj2,
                            noun2=n2,
                            noun3=n3,
                            adjective3=adj3,
                            verb1=v1,
                            verb2=verb2,
                            past_verb2=pv2,
                            adjective4=adj4)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)


#in case we need it ... because it fucking took forever to type

 # adjective1=adj1,
 #                            noun1=n1,
 #                            past_verb=pv,
 #                            adverb1=adv1,
 #                            adjective2=adj2,
 #                            noun2=n2,
 #                            noun3=n3,
 #                            adjective3=adj3,
 #                            verb1=v1,
 #                            verb2=verb2,
 #                            past_verb2=pv2,
 #                            adjective4=adj4)
