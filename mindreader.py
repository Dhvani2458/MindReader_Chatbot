# mindreader.py

class ChatNode:
    def __init__(self, question, yes=None, no=None, label=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.label = label

    def is_leaf(self):
        return self.label is not None


class LieDetector:
    def __init__(self):
        self.memory = []

    def remember(self, user_input):
        self.memory.append(user_input)

    def check_for_lies(self):
        # Detect contradictions in the user's input
        if "I never lie" in self.memory and "I lied" in self.memory:
            return "Wait, didn’t you just say you never lie? 🤔"
        return "You seem truthful so far."


def build_mindreader_tree():
    # Creating a decision tree with more layers and complex questions
    return ChatNode(
        "Are you feeling honest today?",
        yes=ChatNode(
            "Do you believe in truth?",
            yes=ChatNode(
                "If you could lie and get away with it, would you?",
                yes=ChatNode(
                    "Interesting. Do you think a lie could ever be justified?",
                    yes=ChatNode(None, label="So you believe some lies are acceptable... 🤨"),
                    no=ChatNode(None, label="You would never justify a lie. You're a purist! 😇")
                ),
                no=ChatNode(
                    "Do you think all truths are absolute?",
                    yes=ChatNode(None, label="You see truth as a fixed concept. 🧠"),
                    no=ChatNode(None, label="You're open-minded and flexible about truth! 🧐")
                )
            ),
            no=ChatNode(
                "Do you think honesty is always the best policy?",
                yes=ChatNode(
                    "Have you ever told a white lie? (Small but harmless)",
                    yes=ChatNode(None, label="Everyone does it, right? 😅"),
                    no=ChatNode(None, label="Wow, you stick to your guns! 😲")
                ),
                no=ChatNode(None, label="You don’t care for honesty much, huh? 🤔")
            )
        ),
        no=ChatNode(
            "Are you trying to hide something?",
            yes=ChatNode(
                "Have you ever committed a 'perfect' crime?",
                yes=ChatNode(
                    "Was it a big crime or a small one?",
                    yes=ChatNode(None, label="You’re a mastermind. 😈"),
                    no=ChatNode(None, label="A petty crime, huh? Sneaky! 😜")
                ),
                no=ChatNode(None, label="You’re not as sneaky as you think. 😏")
            ),
            no=ChatNode(
                "Would you betray someone for personal gain?",
                yes=ChatNode(None, label="A bit of a dark side, I see... 😈"),
                no=ChatNode(None, label="You're loyal and noble. I can respect that! 😇")
            )
        )
    )

def start_chat(tree):
    current_node = tree
    while not current_node.is_leaf():
        print(current_node.question)
        response = input("Your answer: ").strip()

        # Remembering user input and checking for contradictions
        response_normalized = response.strip()
        
        # Record the answer and check for contradictions
        if response_normalized:
            if "yes" in response_normalized.lower():
                current_node = current_node.yes
            else:
                current_node = current_node.no
        else:
            print("Please provide a valid answer. (Don't leave it blank!)")
            continue
        
    print(current_node.label)
