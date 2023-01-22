from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# custom responces
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#custom text 
helpOptions= [


"help",
"i can help you out. here are some key words 'help navigate' or 'what are yo'",
"",
"",
]

# Set the trainers we want train
trainer_personality_snow=ListTrainer(english_bot)
#for custom texts
trainer_personality_snow.train(helpOptions)


trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations",
              "chatterbot.corpus.english.ai",
              "chatterbot.corpus.english.money"
              
              
              )



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run()
