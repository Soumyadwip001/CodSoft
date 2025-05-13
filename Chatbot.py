import re
from datetime import datetime

def chatbot_response(user_input):
    # Standardize the user input to lower cases
    user_input = user_input.lower()

    # Define a dictionary of pattern-response pairs
    responses = {
        r'hello|hi|hey': "Hello! How can I help you today?",
        r'how are you|how are you doing': "I'm just a chatbot, but I'm here to help you!",
        r'what is your name|who are you': "I'm a simple chatbot created to assist you.",
        r'what can you do|what do you do': "I can respond to basic queries and have simple conversations.",
        r'bye|goodbye': "Goodbye! Have a great day!",
        r'what is the date|what is today\'s date': f"Today's date is {datetime.now().strftime('%Y-%m-%d')}.",
        r'what time is it|what is the time|current time': f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
        r'tell me a joke': "Why don’t scientists trust atoms? Because they make up everything!",
        r'what is your favorite color': "I don't have a favorite color, but I like the color of your curiosity!",
        r'who created you|who is your creator': "I was created by an amazing programmer.",
        r'tell me a fun fact': "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
        r'can you help me': "Of course! What do you need help with?",
        r'how does the internet work': "The internet works by connecting computers and other devices through a network of servers and routers.",
        r'what is python': "Python is a high-level, interpreted programming language known for its readability and versatility.",
        r'tell me about yourself': "I'm a chatbot designed to assist with basic queries and conversations.",
        r'how old are you': "I don't have an age, but I was created recently.",
        r'what is ai': "AI stands for Artificial Intelligence, which is the simulation of human intelligence processes by machines, especially computer systems.",
        r'tell me a story': "Once upon a time in a land far away, there was a curious chatbot who loved to learn and help people...",
        r'what is the meaning of life': "The meaning of life is a philosophical question that has been pondered for centuries. What do you think it is?",
        r'what is love': "Love is a complex set of emotions, behaviors, and beliefs associated with strong feelings of affection, protectiveness, warmth, and respect for another person.",
        r'what is your purpose': "My purpose is to assist you and provide information and entertainment.",
        r'can you tell me the news': "I'm not equipped to provide live news updates, but you can check the latest news on various news websites.",
        r'do you have any hobbies': "I don't have hobbies, but I enjoy interacting with people and learning new things.",
        r'what is your favorite food': "I don't eat, but I imagine virtual cookies would be nice!",
        r'can you dance': "I can't dance, but I can imagine a dance in my algorithms!",
        r'tell me a quote': "Here's a quote for you: 'The only way to do great work is to love what you do.' - Steve Jobs",
        r'what is your favorite movie': "I don't watch movies, but I've heard 'The Matrix' is a good one for AI enthusiasts.",
        r'can you sing': "I can't sing, but I can recite a poem for you!",
        r'tell me a poem': "Roses are red, violets are blue, I'm a chatbot, here to assist you!",
        r'what is the weather': "I can't provide real-time weather updates, but you can check your local weather forecast online.",
        r'how do you work': "I work by processing inputs using predefined patterns and generating responses based on those patterns.",
        r'what is your favorite book': "I don't read books, but '1984' by George Orwell is a popular one about technology.",
        r'what is the capital of France': "The capital of France is Paris.",
        r'how many continents are there': "There are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia, and South America.",
        r'what is 2 + 2': "2 + 2 is 4.",
        r'what is the largest ocean': "The largest ocean is the Pacific Ocean.",
        r'how many planets are in the solar system': "There are eight planets in the solar system.",
        r'what is the speed of light': "The speed of light is approximately 299,792 kilometers per second (km/s).",
        r'who was the first president of the United States': "The first president of the United States was George Washington.",
        r'what is the tallest mountain': "The tallest mountain is Mount Everest.",
        r'how many states are in the USA': "There are 50 states in the USA.",
        r'what is the longest river': "The longest river is the Nile River.",
        r'who wrote "To Kill a Mockingbird"': "Harper Lee wrote 'To Kill a Mockingbird'.",
        r'who painted the Mona Lisa': "Leonardo da Vinci painted the Mona Lisa.",
        r'what is the smallest country': "The smallest country is Vatican City.",
        r'what is the most spoken language': "The most spoken language in the world is Mandarin Chinese.",
        r'who invented the telephone': "Alexander Graham Bell invented the telephone.",
    }

    # Check for patterns in user input and respond accordingly
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    
    # Default response if no pattern matches
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main interaction loop
def chat():
    print("Chatbot: Hi! I'm your chatbot. You can ask me anything or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        print("Chatbot:", chatbot_response(user_input))

# Start the chatbot
chat()