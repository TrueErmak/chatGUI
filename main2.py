# Code based on https://www.geeksforgeeks.org/text-to-speech-changing-voice-in-python/

# Python program to show
# how to convert text to speech
import pyttsx3

# Initialize the converter
converter = pyttsx3.init()

# Set properties before adding
# Things to say

# Sets speed percent
# Can be more than 100
converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 0.7)

# Queue the entered text
# There will be a pause between
# each one like a pause in
# a sentence
converter.say("Hello Kate")
converter.say("I also like AI")

# Gets and prints list of voices available
voices = converter.getProperty('voices')

# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()

'''for voice in voices:
    # to get the info. about various voices in our PC
    print("Voice:")
    print("ID: %s" % voice.id)
    print("Name: %s" % voice.name)
    print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    print("Languages Known: %s" % voice.languages)'''

# Now configure for female voice
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# or male ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0


# Use female voice
converter.setProperty('voice', voice_id)
converter.say("Kate, do I sound different to you now?")
converter.runAndWait()

