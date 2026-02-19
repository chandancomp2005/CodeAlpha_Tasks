import random
import time


def get_reply(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hi! 😊",
            "Hello! How can I help you? 😄",
            "Hey! Nice to see you! 👋"
        ])

    # How are you
    elif "how are you" in user_input:
        return random.choice([
            "I'm doing great! Thanks for asking 😄",
            "I'm fine! What about you? 😊",
            "All good here! 🚀"
        ])

    # Bot name
    elif any(word in user_input for word in ["your name", "who are you"]):
        return "I am a simple rule-based chatbot 🤖"

    # Time
    elif "time" in user_input:
        current_time = time.strftime("%I:%M %p")
        return f"Current time is {current_time} ⏰"

    # Help
    elif "help" in user_input:
        return ("I can respond to:\n"
                "- hello / hi / hey\n"
                "- how are you\n"
                "- your name\n"
                "- time\n"
                "- bye")

    # Bye
    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a nice day 👋😊"

    # Default response
    else:
        return random.choice([
            "Sorry, I didn't understand that 😅",
            "Can you say that in a different way?",
            "Hmm... I am not sure about that 🤔"
        ])


def chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Chatbot:", reply)

        if any(word in user_input.lower() for word in ["bye", "exit", "quit", "goodbye"]):
            break


# Run chatbot
chatbot()
