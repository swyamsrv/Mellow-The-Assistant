import datetime as datetime
import pyttsx3
import pywhatkit
# import datetime
# import webbrowser
# from bs4 import BeautifulSoup
# from time import sleep, strftime
# import os
from datetime import timedelta
import speech_recognition as sr
from datetime import datetime

swy_mello = pyttsx3.init()


def speak(audio):
    """This Function is used for speaking the command given by computer as which is in the form of text"""

    voices = swy_mello.getProperty('voices')
    swy_mello.setProperty('voice', voices[0].id)  # changing index changes voices but ony 0 and 1 are working here
    swy_mello.setProperty('rate', 185)  # Rate of audio
    swy_mello.setProperty('volume', 1)  # MAX Volume = 1 and it alters between (0 - 1)
    swy_mello.say(audio)
    swy_mello.runAndWait()  # RunAndWait() - This function will make the speech audible in the system
    # if you don't write this command then the speech will not be audible to you


def take_command():  # It uses speech recognition library for taking input....

    """Recognizes the audio and sends it for display to displayText."""

    r = sr.Recognizer()  # Speech recognition helps you to save time by speaking instead of typing.
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
        audio = r.listen(source, 0, 4)  # listen for the first phrase and extract it into audio data,
        # wait for 5 seconds

        try:
            print('Recognizing....')
            query = r.recognize_google(audio, language='en-US')
            query = query.lower()
            print(query)
            # put = r.recognize_google(audio)

        except Exception as e:
            print(e)
            # speak("Please Say that again")
            return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak('Who do you want to Message, For example say 1 for first person')
    print("""
    Person - 1-> Harsh
    Person - 2 -> Harsh
    Person - 3 -> Mummy
    Person - 4 -> Didi
    Person - 5 -> Bhavesh
    Person - 6 -> Divyansh
    Person - 7 -> Ashutosh
    Person - 8 -> Samarth
    Person - 9 -> Dipanshu
    Person - 10 -> Arsh
    Person - 11 -> Vivek
    Person - 12 -> Yogesh
    \n""")
    a = take_command()
    if int(a) == 1:  # Harsh
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+919935114194", message, time_hour=strTime, time_min=update)

    elif int(a) == 2:  # HARSH2
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+919721472651", message, time_hour=strTime, time_min=update)

    elif int(a) == 3:  # MUMMY
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+917007081992", message, time_hour=strTime, time_min=update)

    elif int(a) == 4:  # DIDI
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+918808697355", message, time_hour=strTime, time_min=update)

    elif int(a) == 5:  # Bhavesh
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+919554938651", message, time_hour=strTime, time_min=update)

    elif int(a) == 6:  # Divyansh
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+918115395532", message, time_hour=strTime, time_min=update)

    elif int(a) == 7:  # ASHUTOSH
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+918172904888", message, time_hour=strTime, time_min=update)

    elif int(a) == 8:   # SAMARTH
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+919648279762", message, time_hour=strTime, time_min=update)

    elif int(a) == 9:  # Dipanshu
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+917266836766", message, time_hour=strTime, time_min=update)

    elif int(a) == 10:  # Arsh
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+917905336341", message, time_hour=strTime, time_min=update)

    elif int(a) == 11:  # Vivek
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+916392970241", message, time_hour=strTime, time_min=update)

    elif int(a) == 12:  # Yogesh
        speak('What is the message')
        message = take_command()
        pywhatkit.sendwhatmsg("+918881007318", message, time_hour=strTime, time_min=update)

    elif a.isalpha() or a > 12:
        speak('Please select a valid option')
        exit()

    speak('Message sent')
    exit()
