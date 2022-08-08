import time
from time import sleep
from googletrans import Translator # pip install googletrans
import googletrans
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound

swy_mello = pyttsx3.init()


def speak(audio):

    """This Function is used for speaking the command given by computer as which is in the form of text"""

    voices = swy_mello.getProperty('voices')
    swy_mello.setProperty('voice', voices[0].id)  # changing index changes voices but ony 0 and 1 are working here
    swy_mello.setProperty('rate', 185)  # Rate of audio
    swy_mello.setProperty('volume', 1)    # MAX Volume = 1 and it alters between (0 - 1)
    swy_mello.say(audio)
    swy_mello.runAndWait()  # RunAndWait() - This function will make the speech audible in the system
    # if you don't write this command then the speech will not be audible to you


def take_command():  # It uses speech recognition library for taking input....

    """Recognizes the audio and sends it for display to displayText."""

    r = sr.Recognizer()   # Speech recognition helps you to save time by speaking instead of typing.
    # It helps us to communicate with our devices without writing one line of code

    with sr.Microphone() as source:
        # playsound.playsound("Mello_activation.wav")
        # pygame.mixer.init()
        # pygame.mixer.music.load('Mello_activation.wav')
        # pygame.mixer.music.play()
        print("Listening.......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        # speak.runAndWait()    # This function will make the speech audible in the system,
        # if you don't write this command then the speech will not be audible to you
        audio = r.listen(source, 0, 4)   # listen for the first phrase and extract it into audio data,
        # wait for 5 seconds

        try:
             print('Recognizing....')
             query = r.recognize_google(audio, language='en-US')
             query = query.lower()
             print(query)
             # put = r.recognize_google(audio)

        except Exception as e:
            # speak("Please Say that again")
             print(e)
             return "None"

    return query

def translate(query):
    speak('sure sir')
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language to translate")
    b = input('TO Language:- ')
    text_to_translate = translator.translate(query, src='auto', dest = b )
    text = text_to_translate.text

    try:
        speakgl = gTTS(text = text, lang = b, slow = False)
        speakgl.save('voice.mp3')
        playsound('voice.mp3')
        time.sleep(5)
        os.remove('voice.mp3')
    except:
        print('Unable to translate\n')
        speak('Unable to translate')