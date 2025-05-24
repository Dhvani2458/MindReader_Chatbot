# main.py
from mindreader import ChatNode, LieDetector, build_mindreader_tree, start_chat

def chatbot_game():
    print("🎭 Welcome to the Mindreader Chatbot Game! (Answer freely!)\n")

    # Ask role, name, gender
    role = input("Are you a student or faculty? ").strip().lower()
    name = input("What is your name? ").strip()
    gender = input("What is your gender? (male/female/other): ").strip().lower()

    print(f"\nAwesome, {name}! Let’s begin the game...\n")

    # Initialize the lie detector and tree
    bot = LieDetector()
    tree = build_mindreader_tree()

    while True:
        user_input = input("\nYou: ").strip()

        if "bye" in user_input.lower():
            # Customized goodbye messages
            if role == "faculty":
                print(f"Goodbye {name.title()} ma'am, your wisdom is always appreciated! 👩‍🏫")
            elif role == "student":
                if gender == "male":
                    print(f"Goodbye {name.title()}, stay smart and smooth, king 👑")
                elif gender == "female":
                    print(f"Goodbye {name.title()}, keep shining and slaying, queen 👸")
                else:
                    print(f"Goodbye {name.title()}, you’re one of a kind – never stop being you 🌈")
            else:
                print(f"Goodbye {name.title()}! You're a mystery, and I like that 😉")
            break

        # Store and analyze user's response
        bot.remember(user_input)
        print(bot.check_for_lies())

        # Continue with the mindreader tree chat
        start_chat(tree)

if __name__ == "__main__":
    chatbot_game()
