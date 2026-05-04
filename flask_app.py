from flask import Flask, render_template, request


app = Flask(__name__)

dragon = {
    "egg": None,
    "type": None,
    "name": "Drako",
    "level": 1,
    "hunger": 5,
    "happiness": 5
}

@app.route("/")
def choose():
    return render_template("result.html")

@app.route("/choice", methods=["POST"])
def choice():
    dragon["egg"] = request.form["egg"]
    return render_template("hatch.html", egg=dragon["egg"], hatched=False)
    '''
    <h1>Choose Your Dragon Egg</h1>

    <form action="/choose" method="POST">
        <button name="egg" value="Fire Egg">🔥 Fire Egg</button>
        <button name="egg" value="Ice Egg">❄️ Ice Egg</button>
        <button name="egg" value="Storm Egg">⚡ Storm Egg</button>
        <button name="egg" value="Shadow Egg">🌑 Shadow Egg</button>
    </form>
    '''


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
    '''
    <h1>Dragon Hatching</h1>

    {% if not hatched %}

    <p>{{ egg }} is shaking...</p>

    <form action="/hatch" method="POST">
    <button type="submit">Hatch Egg</button>
    </form>

    {% else %}

    <h2>You got a {{ dragon }} Dragon!</h2>

    <a href="/start">Start Raising Your Dragon</a>

    {% endif %}
    '''


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
    '''
    <h1>Your Dragon</h1>

    <p>Type: {{ dragon.type }}</p>
    <p>Level: {{ dragon.level }}</p>
    <p>Hunger: {{ dragon.hunger }}</p>
    <p>Happiness: {{ dragon.happiness }}</p>

    <form method="POST">
        <button name="action" value="feed">Feed</button>
        <button name="action" value="train">Train</button>
        <button name="action" value="play">Play</button>
    </form>
    '''
