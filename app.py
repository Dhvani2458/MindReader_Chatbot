from flask import Flask, render_template, request, jsonify
from mindreader import LieDetector, build_mindreader_tree, start_chat

app = Flask(__name__)
bot = LieDetector()
tree = build_mindreader_tree()
chat_node = [tree]  # Mutable wrapper to hold current node

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_game():
    # Get the user's name from the request data
    data = request.json
    name = data.get("name", "").strip()
    
    if not name:
        return jsonify({"message": "Name is required!"}), 400

    # Initialize the chatbot (optionally, start the game with a greeting)
    chat_node[0] = tree  # Start from the root node of the decision tree

    # Send the first message/question to the user
    first_question = chat_node[0].question
    return jsonify({"message": f"Welcome, {name}! Let’s begin the game... {first_question}"})


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip().lower()

    if user_input:
        bot.remember(user_input)
        lie_check = bot.check_for_lies()
        
        current = chat_node[0]

        if current.is_leaf():
            return jsonify({"response": current.label, "end": True})

        # Navigate the decision tree based on the user input
        if "yes" in user_input:
            chat_node[0] = current.yes
        else:
            chat_node[0] = current.no

        if chat_node[0].is_leaf():
            return jsonify({"response": chat_node[0].label, "lieCheck": lie_check, "end": True})
        else:
            return jsonify({"response": chat_node[0].question, "lieCheck": lie_check, "end": False})
    
    return jsonify({"response": "Please provide a valid answer."})

if __name__ == "__main__":
    app.run(debug=True)
