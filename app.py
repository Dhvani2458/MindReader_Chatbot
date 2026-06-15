from flask import Flask, render_template, request, jsonify, session
from mindreader import LieDetector, build_mindreader_tree

app = Flask(__name__)
app.secret_key = "mindreader_secret"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():

    data = request.json

    session["role"] = data["role"]
    session["name"] = data["name"]
    session["gender"] = data["gender"]

    session["memory"] = []
    session["current_path"] = []

    tree = build_mindreader_tree()

    return jsonify({
        "message":
        f"Awesome, {data['name']}! Let's begin the game...<br><br>{tree.question}"
    })


@app.route("/chat", methods=["POST"])
def chat():

    user_input = request.json["message"].strip()

    # Initialize chatbot state
    if "memory" not in session:
        session["memory"] = []

    if "current_path" not in session:
        session["current_path"] = []

    # Goodbye Logic
    if "bye" in user_input.lower():

        role = session.get("role", "")
        name = session.get("name", "")
        gender = session.get("gender", "")

        if role == "faculty":
            msg = f"Goodbye {name.title()} ma'am, your wisdom is always appreciated! 👩‍🏫"

        elif role == "student":

            if gender == "male":
                msg = f"Goodbye {name.title()}, stay smart and smooth, king 👑"

            elif gender == "female":
                msg = f"Goodbye {name.title()}, keep shining and slaying, queen 👸"

            else:
                msg = f"Goodbye {name.title()}, you're one of a kind – never stop being you 🌈"

        else:
            msg = f"Goodbye {name.title()}! You're a mystery, and I like that 😉"

        return jsonify({
            "reply": msg,
            "end": True
        })

    # Lie Detector
    bot = LieDetector()

    for msg in session["memory"]:
        bot.remember(msg)

    bot.remember(user_input)

    memory = session["memory"]
    memory.append(user_input)
    session["memory"] = memory

    lie_message = bot.check_for_lies()

    # Build Tree
    tree = build_mindreader_tree()

    current = tree

    # Reconstruct position in tree
    for step in session["current_path"]:

        if step == "yes":
            current = current.yes
        else:
            current = current.no

    # First question
    if len(session["current_path"]) == 0 and len(session["memory"]) == 1:

        return jsonify({
            "reply": f"{lie_message}<br><br>{current.question}",
            "end": False
        })

    # Move tree forward
    if "yes" in user_input.lower():

        if current.yes:
            current = current.yes

        path = session["current_path"]
        path.append("yes")
        session["current_path"] = path

    else:

        if current.no:
            current = current.no

        path = session["current_path"]
        path.append("no")
        session["current_path"] = path

    # Leaf node
    if current.is_leaf():

        session["current_path"] = []

        return jsonify({
            "reply": f"{lie_message}<br><br>{current.label}",
            "end": False
        })

    return jsonify({
        "reply": f"{lie_message}<br><br>{current.question}",
        "end": False
    })


if __name__ == "__main__":
    app.run(debug=True)