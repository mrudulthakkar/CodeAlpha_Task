import random
import datetime

# Function to handle chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Rule-based replies
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help you?"])

    elif "how are you" in user_input:
        return random.choice(["I'm doing great, thanks!", "Feeling awesome today!", "I'm fine, how about you?"])

    elif "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

    elif "date" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"

    else:
        return random.choice([
            "Sorry, I didn't get that.",
            "Can you rephrase?",
            "Hmm, that's interesting!"
        ])

# Main chatbot loop
def run_chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_message = input("You: ")
        response = chatbot_response(user_message)
        print("🤖 Chatbot:", response)

        if "bye" in user_message.lower():
            break

# Run chatbot
if __name__ == "__main__":
    run_chatbot()
