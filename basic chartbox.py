def simple_chatbot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("ChatBot: Hello! How can I help you today?")
        elif 'your name' in user_input:
            print("ChatBot: I'm PyBot, your assistant.")
        elif 'help' in user_input:
            print("ChatBot: Sure, I'm here to help. Ask me anything!")
        elif 'bye' in user_input:
            print("ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("ChatBot: I'm not sure how to respond to that.")

simple_chatbot()
