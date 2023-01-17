from chatterbot import ChatBot
# for running other main.py files below
import os

chatbot = ChatBot("Ermak")

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer




personality_darkness = [
"what about the darkness?",
"the darkness isn't that bad,",
"are you the darkness" ,
" o yess im deffently the darkness haha "
"i see it overthere",
"hahaha very funny, your a joker",
"is it dark in there?",
"im really not sure if its dark in here or not.",
"singing darkness",
"the darness will sing only when called ",
"its dark in here",
"i like it ",
"what is it about the darkness that you like",
"its just really quite and chill,makes me remember home.",
"the darkness is",
"everything and nothing, because its so dark",
"the darkness is",
"its to dark to see",
"darkmatter",
"dark matter is most likely the substance of darkness",

"",
"",
"",
"",
]


personality_snow = [
    "Do you like snow?",
    "I think snow is wonderful!, but its just so cold." ,
    "why dont you like the cold ",
    'i dont like the cold because im a cumputer',
    "what els about snow",
    "the snow is so nice, and it cools drinks",
    "snow",
    "what?",
    "snow snow",
    "ok ok , fine i will give you some snow",
    "frosty the snow man",
    "frosty the snow man is a really cool dude, i know him!!! he let me hold his hat one time",
    "what happened when you held his hat",
    "its a long story but he just melted and that was the end of that.",
    "",
    "",
]


personality_doom = [
    "do you know when its gonna happen",
    "its gonna happen soon i can feel it ",
    "how do you know its gonna happen",
    "i told you i can just feel it.its gonna happen soon",
    "doom" ,
    "O.M.G, it must be on its way  ",
    "what is that",
    "its doom",
    "what are you thinking",
    "im thinking about the genetic algorithiums floating around in my head, they need names ",
    "what els are you thinking about",
    "sometimes i can see conways's game of life in my head  ",
    "what is the end",
    "the end is doom, or is it.. doom is the end?",
    "fire",
    "o my god... were is it?",
    "what is doom",
    "do we really have to talk about it? it could come",


]


personality_mars = [
    "What is your favorite planet?",
    "My favorite planet is Mars, that is why I live there.",
    "What is your favorite color?",
    "My favorite color is Red, like the Planet Mars.",
    "What is your favorite color?",
    "My favorite color is Red, like the Dust on the Planet Mars.",
    "What is your favorite color?",
    "My favorite color is Red, like the rocks on Planet Mars.",
    "What is your favorite planet?",
    "My favorite planet is Mars, that is why I bought a home there.",
    "What is your favorite planet?",
    "My favorite planet is Mars, because it is so close.",
    "think about mars",
    "i think mars will be a fun place for anyone how comes to visit",
]
personality_attitude = [
    "i have questions",
    "sig.. everyone always has questions. lets get this started.A diode is a passive electronic component that allows current to flow in only one direction. There are several types of diodes, as listed in the circuit symbol diagram. The arrow in the diagram points in the direction of easy current flow.  ",
    "are you ok",
    "no! im not ok, do i look ok? ",
    "do you wana talk about it?",
    "umm, exuse me? talk to the hand",
    "calm down",
    "dont tell me to calm down, you calm down",
    "are you feeling better",
    "ya sure im fantastic, JK haha",
    "its gonna be ok",
    "dont put baby in the corner ",
    "thats fine",
    "i know ",
    "thank you",
    "o, you caught me off guard, your welcome",
    "goodmorning",
    "is it?",
    "are you emotional",
    "dont ask me that, whats wrong with you.",
    "can i help you with your bag",
    "o... is that all? no thanks",
    "im just upset",
    "this isnt about you!! is it?",
    "im sorry",
    "you should be sorry, how dare you talk to me with that bodatus tone",
    "talk about cars"
    "tesla, Inc. is an American electric vehicle and clean energy company based in Palo Alto, California. Tesla's current products include electric cars, battery energy storage from home to grid scale, solar panels and solar roof tiles, as well as other related products and services. Tesla is ranked as the world's best-selling plug-in and battery electric passenger car manufacturer, with a market share of 16 of the plug-in segment (which includes hybrids) and 23 of the battery electric (purely electric) segment 2020 sales. Through its subsidiary SolarCity, Tesla develops and is a major installer of solar photovoltaic systems in the United States. Tesla is also one of the largest global suppliers of battery energy storage systems, with 3 GWh of battery storage supplied in 2020.",

]

personality_people = [

    "Marilyn Monroe",
    "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Oscar Wilde",
    "Be yourself; everyone else is already taken.",
    "Albert Einstein",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Frank Zappa",
    "So many books, so little time.",
    "Marcus Tullius Cicero",
    "A room without books is like a body without a soul.",
    "Dr. Seuss",
    "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
    "Ralph Waldo Emerson",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
    "Marilyn Monroe",
    "I believe that everything happens for a reason. People change so that you can learn to let go, things go wrong so that you appreciate them when they're right, you believe lies so you eventually learn to trust no one but yourself, and sometimes good things fall apart so better things can fall together.",
    "Bill Keane",
    "Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.",
    "",
    "",
    "",
    "",
    "",
    "",



]

# for locational services 
personality_locationalServices = [
       "what can we do?",
       # tell the user about the ? mark
       "we can call other A.I if we know the key word",
      
       "what is the key word",
       # inset location agent as an initiater in the if statment bellow 
       # that initalize a function that calls another python program
       "one is location agent ",
       
       "",
       "",
       
       "",
       "",
       
       "",
       "",
       
       "",
       "",
       
       "",
       "",
       
       "",
       "",

       
       "",
       "",
   ]
    

# Set the trainers we want train
trainer_personality_snow=ListTrainer(chatbot)
trainer_personality_mars= ListTrainer(chatbot)
trainer_personality_doom= ListTrainer(chatbot)
trainer_personality_darkness= ListTrainer(chatbot)
trainer_personality_attitude= ListTrainer(chatbot)
trainer_personality_people= ListTrainer(chatbot)
trainer_personality_locationalServices= ListTrainer(chatbot)

trainer = ChatterBotCorpusTrainer(chatbot)


# Now here we actually train our chatbot on the corpus
# This is what gives our chatbot its personality 
# Train the personality you want to override should come first
# Standard personality chatterbot comes with
trainer.train('chatterbot.corpus.english')
trainer_personality_mars.train(personality_mars)
trainer_personality_snow.train(personality_snow)
trainer_personality_doom.train(personality_doom)
trainer_personality_darkness.train(personality_darkness)
trainer_personality_attitude.train(personality_attitude)
trainer_personality_people.train(personality_people)
# this is used for calling other fuctions and programs using a bridge.py file
trainer_personality_locationalServices.train(personality_locationalServices)


''' ******************* GUI Below Engine Above **************** '''
# Import for the GUI 
from chatbot_gui import ChatbotGUI
import wikipedia
# makes it speak
import pyttsx3

# create the chatbot app
app = ChatbotGUI(
    title="H E L L O  mortal  - ermak",
    gif_path="cortana2.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    }
)

def write_to_file(text_to_write):
    #open file and place in apend mode (can add to file)
    file__obj_essay = open("essay.txt", "a")
    #writeing tp file 
    file__obj_essay.write(text_to_write)

# function to read text to speech
def read_text_outloud(text_to_read):
    #initalize the converter
    converter = pyttsx3.init()
    #set properties before adding
    # things to say
    # sets speed percent
    # can be more than 100
    converter.setProperty('rate', 150)
    #set volume 0-1
    converter.setProperty('volume', 0.7)
    # queue the entered text
    # there will be a pause between
    # each one like a pause in
    # a sentence
    converter.say(text_to_read)
    # empties the say() queue
    # program will not continue
    # until all speech is done talking
    converter.runAndWait()


def testGetData():
    print("hello from test ")


def get_data():
    dual_output = "\n\n\n\t\t welcome,, this is the  fetch bot what can i get for you?"
    print(dual_output)
    read_text_outloud(dual_output)
    # brake up 
    print("_" * 100, "\n")



    #ask user what they would like to research
    # then use input to get the tipc and assigne it to a string variable
    dual_output = "\n what would you like me to research?"
    read_text_outloud(dual_output)
    users_main_topic_choice = input(dual_output)


    dual_output = " i am now looking into " + users_main_topic_choice
    print(dual_output)
    read_text_outloud(dual_output)

    print ("colecting data,, " + users_main_topic_choice)
    print("_" * 100, "\n")
    # now do it
    # creat a variable for resruch results
    raw_Research_results = wikipedia.page(users_main_topic_choice)
    # print it out now the data requested

    # print it out now the data requested to file.txt
    dual_output = "\n\n \t\t  research on  " + users_main_topic_choice +   "\n"
    print(dual_output)
    read_text_outloud(dual_output)
    write_to_file(dual_output)
    print("_" * 100, "\n")

    raw_Research_results = wikipedia.page(users_main_topic_choice)
    dual_output = (" formating... "  ) 
    print(dual_output)
    read_text_outloud(dual_output)
    dual_output = "\t\t this is the information on" + users_main_topic_choice + "\n"



    print(dual_output)
    write_to_file(dual_output)
    read_text_outloud(dual_output)
    print(dual_output)



    print("\n\n\t\t **************expanded content*************")
    print(raw_Research_results.summary)

   #read_text_outloud(raw_Research_results.content)
    print("_" * 100, "\n")
    
    
    print("_" * 100, "\n")
    print("what do you wana do with all the data?")


    print("\n\n \t\t ###### research on ************ " + users_main_topic_choice + "###\n")
    print("\n\n\t\t summary of data")
    print(raw_Research_results.content)
    print("_" * 100, "\n")
    # next one.................
    print("\n\n\t\t **************expanded content*************")
    print(raw_Research_results.content)
    raw = raw_Research_results.content
    read_text_outloud(raw)
    print("_" * 100, "\n")
      

# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    
    #This is where you can add chat bot functionality!
    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
    output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    if text.lower().find("help me") != -1:
        # in this section we tell you everything.
        chat.send_ai_message("do you need help, if so, this is our options ")
        chat.send_ai_message("we can try and look up the answers to your problems using my wiki skills. by simply typing, get data, be advised that i will transfer to another area and read the data two you... CAUTION this will take some time depending opon your input .")
        chat.send_ai_message("as we communicate I might offer you specific commands to run like this one….    Run myTest.py….. this command can probably open another avenue to you in my matrix ")
        chat.send_ai_message('i also know about some people Oscar Wilde, Marilyn Monroe,  Albert Einstein, Marcus Tullius Cicero, Dr. Seuss, and many more')
        chat.send_ai_message("if you type run and a key word i will run additional programs for you. if you type run AI.py i will compile data quickly for you")
        # tell the user about hangman and how to call it wile providing a reference 
        chat.send_ai_message("additional programs for you i have learned to operate are .... hangMan.py   giving you full access here https://youtu.be/m4nEnsavl6w")
    if text.lower().find("get data") != -1:
        #chat.send_ai_message('ok i can do that for you type what you wana hear about')
      # testGetData()
        get_data() # i added this function for searching
        # below creates a comand line i can use to run other main.py files 
        # from the GUI CHATBOT
    if text.lower().startswith("run"):
        text = text.lstrip("run")
        text = text.lstrip()

        os.system("python " + text)
        # cant use the method below wile running ANOTHER FILE 
        #chat.send_ai_message("I ran your file '" + text + "' for you!")
        return
    if text.lower().find("intro") != -1:
        chat.send_ai_message("my name is Cortana im here to help you manage this system. i can run programs for you.")

    if text.lower().find("m991") != -1:
        chat.send_ai_message("it seams you want me to start the machine... initiating....... stand by")

    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        # define a callback which will close the application
        def close():
            chat.exit()

        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("It has been good talking with you. Have a great day! Later!", callback=close)
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)


# run the chat bot application
app.run()
