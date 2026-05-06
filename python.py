from flask import Flask, render_template, request
import random
app = Flask(__name__)

dragon = {
    "egg": None,
    "type": "Unknown",
    "stage": "Baby",
    "level": 1,
    "hunger": 5,
    "happiness": 5,
    "energy": 5
}

@app.route("/")
def choose():
    return render_template("select.html")

@app.route("/choose", methods=["POST"])
def choice():
    egg = request.form["egg"]

    dragon["egg"] = egg
    dragon["hatch_progress"] = 0

    return render_template(
        "hatch.html",
        egg=egg,
        hatched=False,
        dragon=dragon
    )
    return render_template("hatch.html", egg=egg)

@app.route("/hatch", methods=["POST"])
def hatch():
    method = request.form["method"]
    egg = dragon["egg"]

    if method == "wait":
        dragon["hatch_progress"] += 1

    elif method == "magic":
        dragon["hatch_progress"] += 1
        if random.random() < 0.2:
            dragon["hatch_progress"] -= 1
        elif random.random() > 0.5:
            dragon["hatch_progress"] += 3

    dragon["hatch_progress"] = max(0, min(dragon["hatch_progress"], 5))

    if dragon["hatch_progress"] >= 5:

        if random.random() < 0.1:
            dragon["type"] = "Legendary"
        else:
            if egg == "Fire Egg":
                dragon["type"] = "Fire"
            elif egg == "Ice Egg":
                dragon["type"] = "Ice"
            else:
                dragon["type"] = "Unknown"

        return render_template("hatch.html", egg=egg, hatched=True, dragon=dragon["type"])

    return render_template("hatch.html", egg=egg, hatched=False, dragon=dragon)

@app.route("/dragon", methods=["GET", "POST"])
def dragon_page():

    message = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "feed":
            dragon["hunger"] += 2
            message = "Fed!"

        elif action == "train":
            dragon["level"] += 1
            dragon["energy"] -= 1
            message = "Trained!"

        elif action == "play":
            dragon["happiness"] += 2
            dragon["energy"] -= 1
            message = "Played!"

        elif action == "rest":
            dragon["energy"] += 2
            message = "Rested!"

    dragon["hunger"] = max(0, min(dragon["hunger"], 10))
    dragon["happiness"] = max(0, min(dragon["happiness"], 10))
    dragon["energy"] = max(0, min(dragon["energy"], 10))

    if dragon["level"] >= 5:
        dragon["stage"] = "Adult"
    elif dragon["level"] >= 2:
        dragon["stage"] = "Young"
    else:
        dragon["stage"] = "Baby"

    return render_template("dragon.html", dragon=dragon, message=message)

