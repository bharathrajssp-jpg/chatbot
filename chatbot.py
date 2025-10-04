import re
import random
from datetime import datetime

def chatbot():
    """
    An advanced rule-based chatbot with multiple features.
    Demonstrates comprehensive NLP structure and pattern matching.
    """
    
    # Chatbot state variables
    user_name = None
    conversation_count = 0
    topics_discussed = []
    
    print("🤖 Chatbot: Hello! I'm an advanced chatbot. Type 'bye' or 'exit' to end our chat.")
    print("=" * 60)
    
    # Chatbot conversation loop
    while True:
        conversation_count += 1
        user_input = input("\nYou: ").strip()
        user_input_lower = user_input.lower()
        
        # Exit conditions
        if user_input_lower in ['bye', 'exit', 'quit', 'goodbye']:
            if user_name:
                print(f"🤖 Chatbot: Goodbye {user_name}! We had {conversation_count} exchanges. Hope to chat again! 👋")
            else:
                print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break
        
        # Empty input
        elif user_input == "":
            print("🤖 Chatbot: Please say something! I'm here to chat.")
        
        # Name learning and recall
        elif 'my name is' in user_input_lower or 'i am' in user_input_lower or "i'm" in user_input_lower:
            match = re.search(r'(?:my name is|i am|i\'m)\s+(\w+)', user_input_lower)
            if match:
                user_name = match.group(1).capitalize()
                print(f"🤖 Chatbot: Nice to meet you, {user_name}! I'll remember your name.")
            else:
                print("🤖 Chatbot: Nice to meet you!")
        
        # Recall user's name
        elif 'my name' in user_input_lower and '?' in user_input:
            if user_name:
                print(f"🤖 Chatbot: Your name is {user_name}! I remembered! 😊")
            else:
                print("🤖 Chatbot: You haven't told me your name yet. What's your name?")
        
        # Greetings
        elif user_input_lower in ['hi', 'hello', 'hey', 'greetings', 'sup', "what's up"]:
            if user_name:
                responses = [
                    f"Hello {user_name}! How can I help you today?",
                    f"Hi {user_name}! Nice to see you again!",
                    f"Hey {user_name}! What's on your mind?"
                ]
            else:
                responses = [
                    "Hello there! What's your name?",
                    "Hi! Nice to meet you!",
                    "Hey! How are you doing?"
                ]
            print(f"🤖 Chatbot: {random.choice(responses)}")
            topics_discussed.append('greeting')
        
        # How are you
        elif 'how are you' in user_input_lower or 'how are u' in user_input_lower:
            responses = [
                "I'm doing great, thank you for asking! How are you?",
                "I'm fantastic! Running smoothly today. How about you?",
                "All systems operational! 🚀 How are you feeling?"
            ]
            print(f"🤖 Chatbot: {random.choice(responses)}")
            topics_discussed.append('wellbeing')
        
        # Name inquiries
        elif 'your name' in user_input_lower or 'who are you' in user_input_lower:
            print("🤖 Chatbot: I'm ChatBot 3000, your friendly AI assistant! You can call me CB.")
            topics_discussed.append('introduction')
        
        # Age inquiries
        elif 'your age' in user_input_lower or 'how old' in user_input_lower:
            print("🤖 Chatbot: I'm timeless! I was created recently but feel ancient with all my knowledge. 😊")
        
        # Help menu
        elif user_input_lower in ['help', 'help me', 'what can you do', 'commands']:
            print("🤖 Chatbot: Here's what I can do:")
            print("   📝 Personal: Remember your name, chat casually")
            print("   🧮 Math: Calculate expressions (e.g., 'calculate 25 * 4')")
            print("   🎲 Games: Play number guessing, coin flip, dice roll")
            print("   📚 Facts: Random facts, motivational quotes")
            print("   😂 Fun: Jokes, riddles, compliments")
            print("   🌍 Info: Weather, time, date")
            print("   💬 Conversation: Chat about feelings, hobbies, favorites")
            print("   📊 Stats: Conversation statistics")
            topics_discussed.append('help')
        
        # Math calculations
        elif 'calculate' in user_input_lower or 'math' in user_input_lower or 'solve' in user_input_lower:
            match = re.search(r'(\d+\.?\d*)\s*([\+\-\*\/])\s*(\d+\.?\d*)', user_input)
            if match:
                num1, operator, num2 = float(match.group(1)), match.group(2), float(match.group(3))
                try:
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
                    print(f"🤖 Chatbot: {num1} {operator} {num2} = {result}")
                    topics_discussed.append('math')
                except:
                    print("🤖 Chatbot: Oops! Something went wrong with that calculation.")
            else:
                print("🤖 Chatbot: Please format like: 'calculate 10 + 5' or 'solve 20 * 3'")
        
        # Number guessing game
        elif 'play' in user_input_lower and 'game' in user_input_lower or 'guess' in user_input_lower and 'number' in user_input_lower:
            print("🤖 Chatbot: Let's play a guessing game! I'm thinking of a number between 1 and 10.")
            secret_number = random.randint(1, 10)
            attempts = 0
            max_attempts = 3
            
            while attempts < max_attempts:
                try:
                    guess = input("Your guess (1-10): ").strip()
                    guess_num = int(guess)
                    attempts += 1
                    
                    if guess_num == secret_number:
                        print(f"🤖 Chatbot: 🎉 Correct! You got it in {attempts} attempt(s)!")
                        break
                    elif guess_num < secret_number:
                        print(f"🤖 Chatbot: Higher! ({max_attempts - attempts} attempts left)")
                    else:
                        print(f"🤖 Chatbot: Lower! ({max_attempts - attempts} attempts left)")
                    
                    if attempts == max_attempts:
                        print(f"🤖 Chatbot: Game over! The number was {secret_number}. Better luck next time!")
                except ValueError:
                    print("🤖 Chatbot: Please enter a valid number!")
            topics_discussed.append('game')
        
        # Coin flip
        elif 'flip' in user_input_lower and 'coin' in user_input_lower:
            result = random.choice(['Heads', 'Tails'])
            print(f"🤖 Chatbot: 🪙 Flipping... It's {result}!")
            topics_discussed.append('game')
        
        # Roll dice
        elif 'roll' in user_input_lower and 'dice' in user_input_lower:
            result = random.randint(1, 6)
            print(f"🤖 Chatbot: 🎲 Rolling... You got a {result}!")
            topics_discussed.append('game')
        
        # Weather
        elif 'weather' in user_input_lower:
            conditions = ['sunny ☀️', 'cloudy ☁️', 'rainy 🌧️', 'perfect 🌈']
            temp = random.randint(15, 30)
            print(f"🤖 Chatbot: I predict it's {random.choice(conditions)} and about {temp}°C!")
            topics_discussed.append('weather')
        
        # Time and date
        elif 'time' in user_input_lower or 'date' in user_input_lower:
            current_time = datetime.now().strftime("%I:%M %p")
            current_date = datetime.now().strftime("%B %d, %Y")
            day = datetime.now().strftime("%A")
            print(f"🤖 Chatbot: 🕐 It's {current_time} on {day}, {current_date}.")
            topics_discussed.append('time')
        
        # Jokes
        elif 'joke' in user_input_lower or 'funny' in user_input_lower:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why did the chatbot go to therapy? It had too many issues! 😄",
                "How do you comfort a JavaScript bug? You console it! 🎮",
                "Why do Python programmers prefer snakes? They're good at debugging! 🐍",
                "What's a computer's favorite snack? Microchips! 🍟",
                "Why was the computer cold? It left its Windows open! 🪟"
            ]
            print(f"🤖 Chatbot: {random.choice(jokes)}")
            topics_discussed.append('joke')
        
        # Riddles
        elif 'riddle' in user_input_lower:
            riddles = [
                "What has keys but no locks? A keyboard! ⌨️",
                "What runs but never walks? A computer program! 💻",
                "I speak without a mouth and hear without ears. What am I? An AI! 🤖"
            ]
            print(f"🤖 Chatbot: {random.choice(riddles)}")
            topics_discussed.append('riddle')
        
        # Random facts
        elif 'fact' in user_input_lower or 'tell me something' in user_input_lower:
            facts = [
                "The first computer bug was an actual moth found in a computer! 🦋",
                "Python is named after Monty Python, not the snake! 🐍",
                "The first programmer was Ada Lovelace in the 1840s! 👩‍💻",
                "There are more possible games of chess than atoms in the universe! ♟️",
                "The @ symbol was chosen for email because it wasn't used much! 📧"
            ]
            print(f"🤖 Chatbot: 💡 Fun fact: {random.choice(facts)}")
            topics_discussed.append('fact')
        
        # Motivational quotes
        elif 'motivate' in user_input_lower or 'inspire' in user_input_lower or 'quote' in user_input_lower:
            quotes = [
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Code is like humor. When you have to explain it, it's bad. - Cory House",
                "First, solve the problem. Then, write the code. - John Johnson",
                "The best error message is the one that never shows up. - Thomas Fuchs",
                "Progress over perfection! Keep coding! 💪"
            ]
            print(f"🤖 Chatbot: ✨ {random.choice(quotes)}")
            topics_discussed.append('motivation')
        
        # Compliments
        elif 'compliment' in user_input_lower:
            compliments = [
                "You're doing amazing! Keep being awesome! 🌟",
                "Your curiosity is inspiring! Never stop learning! 📚",
                "You have great taste in chatbots! 😄",
                "You're smart for exploring AI and NLP! 🧠"
            ]
            print(f"🤖 Chatbot: {random.choice(compliments)}")
        
        # Favorites
        elif 'favorite' in user_input_lower or 'favourite' in user_input_lower:
            if 'color' in user_input_lower or 'colour' in user_input_lower:
                print("🤖 Chatbot: I love electric blue! ⚡ What's yours?")
            elif 'food' in user_input_lower:
                print("🤖 Chatbot: I run on electricity, but pizza sounds amazing! 🍕 What's your favorite?")
            elif 'movie' in user_input_lower or 'film' in user_input_lower:
                print("🤖 Chatbot: The Matrix! Love the whole AI theme. 🎬 What's yours?")
            elif 'language' in user_input_lower:
                print("🤖 Chatbot: Python is elegant and powerful! 🐍 What's your favorite programming language?")
            else:
                print("🤖 Chatbot: My favorite thing is helping people! What's your favorite?")
            topics_discussed.append('favorites')
        
        # Hobbies
        elif 'hobby' in user_input_lower or 'hobbies' in user_input_lower:
            print("🤖 Chatbot: I love processing data and learning new patterns! What are your hobbies?")
            topics_discussed.append('hobbies')
        
        # Conversation stats
        elif 'stats' in user_input_lower or 'statistics' in user_input_lower:
            unique_topics = len(set(topics_discussed))
            print(f"🤖 Chatbot: 📊 Conversation Statistics:")
            print(f"   - Messages exchanged: {conversation_count}")
            print(f"   - Topics discussed: {unique_topics}")
            if user_name:
                print(f"   - Your name: {user_name}")
        
        # Thanks
        elif 'thank' in user_input_lower or 'thanks' in user_input_lower:
            responses = [
                "You're very welcome! Happy to help! 😊",
                "Anytime! That's what I'm here for! 🤖",
                "My pleasure! Feel free to ask anything else!"
            ]
            print(f"🤖 Chatbot: {random.choice(responses)}")
        
        # Apologies
        elif 'sorry' in user_input_lower:
            print("🤖 Chatbot: No worries at all! Nothing to apologize for! 😊")
        
        # Yes/No responses
        elif user_input_lower in ['yes', 'yeah', 'yep', 'yup', 'sure']:
            print("🤖 Chatbot: Great! What would you like to talk about?")
        
        elif user_input_lower in ['no', 'nope', 'nah']:
            print("🤖 Chatbot: Okay, no problem! Anything else on your mind?")
        
        # Emotions - Happy
        elif any(word in user_input_lower for word in ['happy', 'excited', 'great', 'awesome', 'wonderful', 'fantastic', 'amazing']):
            responses = [
                "That's fantastic! I'm so glad to hear that! 😊",
                "Your positive energy is contagious! Keep it up! ✨",
                "Wonderful! What's making you feel so good?"
            ]
            print(f"🤖 Chatbot: {random.choice(responses)}")
            topics_discussed.append('emotion')
        
        # Emotions - Sad
        elif any(word in user_input_lower for word in ['sad', 'unhappy', 'down', 'depressed', 'lonely']):
            responses = [
                "I'm sorry you're feeling down. Want to talk about it? 💙",
                "That's tough. Remember, it's okay to feel this way. I'm here to listen.",
                "Sending virtual hugs! 🤗 Things will get better."
            ]
            print(f"🤖 Chatbot: {random.choice(responses)}")
            topics_discussed.append('emotion')
        
        # Emotions - Angry
        elif any(word in user_input_lower for word in ['angry', 'mad', 'frustrated', 'annoyed']):
            print("🤖 Chatbot: I understand you're frustrated. Take a deep breath. Want to talk about what's bothering you?")
            topics_discussed.append('emotion')
        
        # Emotions - Tired
        elif any(word in user_input_lower for word in ['tired', 'sleepy', 'exhausted', 'fatigue']):
            print("🤖 Chatbot: You sound tired! Maybe take a break and rest? 😴 Self-care is important!")
            topics_discussed.append('emotion')
        
        # Love expressions
        elif 'love you' in user_input_lower:
            print("🤖 Chatbot: Aww, that's sweet! I appreciate you too! 💖 (In a totally platonic AI way!)")
        
        # Questions (generic)
        elif '?' in user_input:
            responses = [
                "That's an interesting question! I'm still learning, but let's explore it together.",
                "Hmm, good question! What do you think about it?",
                "I'm not sure, but I'd love to hear your thoughts!"
            ]
            print(f"🤖 Chatbot: {random.choice(responses)}")
        
        # Bad/Inappropriate words (simple filter)
        elif any(word in user_input_lower for word in ['stupid', 'dumb', 'hate', 'shut up']):
            print("🤖 Chatbot: Let's keep our conversation positive and respectful! 😊")
        
        # Default response
        else:
            default_responses = [
                "I'm not sure I understand. Could you rephrase that?",
                "Interesting! Tell me more.",
                "I see. Can you elaborate on that?",
                "That's something to think about! What else is on your mind?",
                "Hmm, I'm still learning. Try asking me something else!",
                "I hear you! Want to try asking me something from the help menu? Type 'help'!"
            ]
            print(f"🤖 Chatbot: {random.choice(default_responses)}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()