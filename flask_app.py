@app.route("/home")
def home():
    return render_template("select.html")
    '''
    <a>/"choose</a>
    '''

@app.route("/choose", methods=["POST"])
def choose():
    egg = request.form["egg"]
    return render_template("result.html", egg=egg)
    '''
<html>
<head>
    <title>Select Your Dragon Egg</title>
</head>
<body>

<h1>Choose Your Dragon Egg</h1>

<form action="/choose" method="POST">
    <button type="submit" name="egg" value="Fire Egg">Fire Egg</button>
    <button type="submit" name="egg" value="Ice Egg">Ice Egg</button>
    <button type="submit" name="egg" value="Storm Egg">torm Egg</button>
    <button type="submit" name="egg" value="Shadow Egg">Shadow Egg</button>
</form>
</body>
    '''
@app.route("/dragon")
def dragon

