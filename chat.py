import spacy
from datetime import datetime

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define responses for each intent
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "name": ["I'm your friendly chatbot.", "You can call me ChatBuddy."],
    "time": [f"The current time is {datetime.now().strftime('%H:%M:%S')}."],
    "date": [f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}."],
    "location": ["I'm based in the cloud, but you're chatting from Gujarat, India!"],
    "how_are_you": ["I'm just code, but I'm running smoothly! How about you?"],
    "capabilities": ["I can greet you, tell you the time and date, share my name, and more. Try asking!"],
     "president": ["The current president of india is Droupadi Murmu."],
    "day": [f"Today is {datetime.now().strftime('%A')}."],
    "default": ["I'm not sure how to answer that yet. Can you rephrase or ask something else?"]
}

# Intent matcher
def get_intent(text):
    text = text.lower()
    doc = nlp(text)

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(word in text for word in ["thank", "thanks"]):
        return "thanks"
    elif "your name" in text:
        return "name"
    elif "time" in text:
        return "time"
    elif "date" in text or "today" in text:
        return "date"
    elif "where are you" in text or "location" in text:
        return "location"
    elif "how are you" in text:
        return "how_are_you"
    elif "what can you do" in text or "help" in text:
        return "capabilities"
    elif "president" in text:
        return "president"
    elif "day" in text:
        return "day"
    else:
        return "default"

# Chat loop
def chat():
    print("🤖 ChatBot: Hello! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "exit":
            print("🤖 ChatBot: Goodbye!")
            break
        intent = get_intent(user_input)
        print("🤖 ChatBot:", responses[intent][0])

chat()
