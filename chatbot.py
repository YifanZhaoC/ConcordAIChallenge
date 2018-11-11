from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('TourQuebec')

# Create a new trainer for the chatbot
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Train the chatbot based on the english corpus
chatbot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.conversations"
)

# Get a response to an input statement
print(chatbot.get_response("Hello, how are you today?"))
