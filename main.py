from chatterbot import ChatBot
# for running other main.py files below
import os
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
chatbot = ChatBot("Ermak")

temp1 = [


"",
"",
"",
"",
]

temp2 = [
    
    "",
    "",
]

temp3 = [
    


]

temp4 = [
    
]

temp5 = [


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
trainer_personality_mars.train(temp1)
trainer_personality_snow.train(temp2)
trainer_personality_doom.train(temp3)
trainer_personality_darkness.train(temp4)
trainer_personality_attitude.train(temp5)
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
    gif_path="computerGIF.gif", # needs a better handler
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
    if text.lower().find("standUp1") != -1:
        chat.send_ai_message("hello, this is a reporting of the first stand up.  ")
        chat.send_ai_message(" ")
        chat.send_ai_message(" ")


    if text.lower().find("get data") != -1:
        chat.send_ai_message('ok i can do that for you type what you wana hear about')
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
