from main import chatbot_responses
import random

def start():
    """the game start from here"""
    ask = input("Do you want to use Chatbot; type 'Yes' or 'No': ").lower()
    if ask == "yes":
        print("Chatbot: Hello! I'm a simple chatbot. How can I assist you today?")
        repeat()
    elif ask == "no":
        pass
    else:
        print("Wrong input!!")
        start()


def repeat():
    """ask again and again"""
    global human_question
    human_question = input("You: ")
    main()


def main():
    while True:
        if human_question == "quit":
            print(f"Chatbot: {chatbot_responses[human_question]}")
            break
        elif human_question == "goodbye":
            print(f"Chatbot: {chatbot_responses[human_question]}")
            break
        if human_question not in chatbot_responses:
            response = ["Sorry, I cant't accese this.", "I don't understand this ask me other things.","Unable to find solution but i can tell you joke."]
            print(random.choice(response))
            repeat()
        elif human_question in chatbot_responses:
            print(f"Chatbot: {chatbot_responses[human_question]}")
            repeat()


start()
