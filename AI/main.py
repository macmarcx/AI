# Our main file.
import speech_recognition as sr

# Build a recognition
r = sr.Recognizer()

# Open the microphone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)  # Set microphone as audio source

        print(r.recognize_google(audio, language='pt'))
