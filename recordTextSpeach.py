import pyaudio  # pip install pyaudio  brew install portaudio
import wave    

import speech_recognition as sr # for translation  pip install SpeechRecognition pocketsphinx
                                # brew install portaudio


from gtts import gTTS
from playsound import playsound

# Set up PyAudio
p = pyaudio.PyAudio()

# Open a recording stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024)

# Start recording
print("Recording...")
frames = []
for i in range(0, int(44100 / 1024 * 10)):
    data = stream.read(1024)
    frames.append(data)

# Stop recording
stream.stop_stream()
stream.close()
p.terminate()

# Write audio data to file
wf = wave.open("voice.wav", "wb")
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()

print("Voice recorded and saved to 'voice.wav'")


# Create a Recognizer object
r = sr.Recognizer()

# Read the recorded audio file
with sr.AudioFile("voice.wav") as source:
    audio = r.record(source)

# Transcribe the audio
text = r.recognize_google(audio)

# Save the transcript to a .txt file
with open("transcript.txt", "w") as f:
    f.write(text)

print("Transcription saved to 'transcript.txt'")



# Read the transcribed text from the file
with open("transcript.txt", "r") as f:
    text = f.read()

# Convert the text to speech
tts = gTTS(text)

# Save the speech to a file
tts.save("speech.mp3")

# Play the speech file
playsound("speech.mp3")