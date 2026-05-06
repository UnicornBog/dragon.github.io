from flask import Flask, render_template, request
import random
app = Flask(__name__)

dragon = {
    "egg": None,
    "type": "Unknown",
    "level": 1,
    "hunger": 5,
    "happiness": 5,
    "energy": 5,
    "request": "feed",
    "mood": "neutral"
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

    if "request" not in dragon:
        dragon["request"] = generate_request()

    if request.method == "POST":
        action = request.form.get("action")

        if action == dragon["request"]:
            message = "🐉 Your dragon is happy you listened!"
            dragon["happiness"] += 2
            dragon["level"] += 1
        else:
            message = "🐉 Your dragon is a bit disappointed..."

        if action == "feed":
            dragon["hunger"] += 2

        elif action == "train":
            dragon["level"] += 1
            dragon["energy"] -= 1

        elif action == "play":
            dragon["happiness"] += 2
            dragon["energy"] -= 1

        elif action == "rest":
            dragon["energy"] += 2

        dragon["request"] = generate_request()

    dragon["hunger"] = max(0, min(dragon["hunger"], 10))
    dragon["happiness"] = max(0, min(dragon["happiness"], 10))
    dragon["energy"] = max(0, min(dragon["energy"], 10))

    update_mood()

    return render_template("dragon.html", dragon=dragon, message=message)

def update_mood():
    if dragon["energy"] <= 2:
        dragon["mood"] = "sleepy"
    elif dragon["happiness"] >= 7 and dragon["hunger"] >= 4:
        dragon["mood"] = "happy"
    elif dragon["hunger"] <= 3 or dragon["happiness"] <= 2:
        dragon["mood"] = "angry"
    else:
        dragon["mood"] = "neutral"

def generate_request():
    return random.choice([
        "feed",
        "feed",
        "play",
        "rest",
        "train"
    ])

