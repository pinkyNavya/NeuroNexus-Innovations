import re
def simple_chatbot(user_input):
    user_input = user_input.lower()
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewell = ['bye', 'goodbye', 'see you', 'see you later']
    about_bot = ['who are you', 'what are you', 'tell me about yourself']
    favorite_color = ['what is your favourite color', 'your favourite color']
    thanks = ['thank you', 'thanks']
    default_response = "I'm sorry, I don't understand. Can you please rephrase your question?"
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"
    elif any(word in user_input for word in farewell):
        return "Goodbye! Have a great day!"
    elif any(word in user_input for word in about_bot):
        return "I am a simple chatbot. My purpose is to assist and provide information."
    elif any(word in user_input for word in favorite_color):
        return "I don't have a favourite color. I'm just a computer program."
    elif any(word in user_input for word in thanks):
        return "You're welcome!"
    else:
        return default_response
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)