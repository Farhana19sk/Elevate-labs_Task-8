def get_response(user_input: str) -> str:
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! 😊 How can I assist you today?"

    elif "your name" in user_input:
        return "I'm ElevateBot, your friendly Python chatbot!"

    elif "who created you" in user_input:
        return "I was created as part of a Python Developer Internship task."

    elif "help" in user_input:
        return "Sure! You can ask me about greetings, my name, or type 'exit' to quit."

    elif "python" in user_input:
        return "Python is a powerful and easy-to-learn programming language."

    elif user_input in ["exit", "quit", "bye"]:
        return "exit"

    else:
        return "I'm sorry, I don't understand that yet. Try asking something else!"


def main():
    print("=" * 50)
    print("Welcome to ElevateBot (Rule-Based Chatbot)")
    print("Type 'exit' to end the conversation.")
    print("=" * 50)

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        if response == "exit":
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    main()
