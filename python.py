from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple temporary storage
dragon = {
    "egg": None,
    "type": None,
    "name": "Drako",
    "level": 1,
    "hunger": 5,
    "happiness": 5
}

@app.route("/")
def home():
    return render_template("select.html")


@app.route("/choose", methods=["POST"])
def choose():
    dragon["egg"] = request.form["egg"]
    return render_template("hatch.html", egg=dragon["egg"], hatched=False)


@app.route("/hatch", methods=["POST"])
def hatch():
    egg = dragon["egg"]

    if egg == "Fire Egg":
        dragon["type"] = "Fire"
    elif egg == "Ice Egg":
        dragon["type"] = "Ice"
    elif egg == "Storm Egg":
        dragon["type"] = "Storm"
    else:
        dragon["type"] = "Shadow"

    return render_template("hatch.html", egg=egg, hatched=True, dragon=dragon["type"])


@app.route("/dragon", methods=["GET", "POST"])
def dragon_page():
    if request.method == "POST":
        action = request.form["action"]

        if action == "feed":
            dragon["hunger"] += 2
        elif action == "train":
            dragon["level"] += 1
            dragon["hunger"] -= 1
        elif action == "play":
            dragon["happiness"] += 2
            dragon["hunger"] -= 1

    return render_template("dragon.html", dragon=dragon)


@app.route("/start")
def start_game():
    return redirect(url_for("dragon_page"))
