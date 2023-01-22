from flask import Flask, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot("Your_Chatbot_Name")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations",
              "chatterbot.corpus.english.ai",
              "chatterbot.corpus.english.money"
              
              
              )

# custom trainer for things we want the bot to say updated in two places 
trainer = ChatterBotCorpusTrainer(chatbot)



@app.route("/predict", methods=["POST"])
def predict():
    input_text = request.json["input"]
    response = chatbot.get_response(input_text)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)
