import datetime
import pyttsx3
# import os
import time
swy_mello = pyttsx3.init()

import pygame
def speak(audio):

    """This Function is used for speaking the command given by computer as which is in the form of text"""

    voices = swy_mello.getProperty('voices')
    swy_mello.setProperty('voice', voices[0].id)  # changing index changes voices but ony 0 and 1 are working here
    swy_mello.setProperty('rate', 185)  # Rate of audio
    swy_mello.setProperty('volume', 1)    # MAX Volume = 1 and it alters between (0 - 1)
    swy_mello.say(audio)
    swy_mello.runAndWait()  # RunAndWait() - This function will make the speech audible in the system
    # if you don't write this command then the speech will not be audible to you


def wishme():

    """ This function is used to wish the user!! """
    pygame.mixer.init()
    pygame.mixer.music.load("Mello_activation.wav")
    pygame.mixer.music.play()
    time.sleep(1)
    speak('Hello Swyam!!')
    hour = datetime.datetime.now().hour
    # print(hour)
    if hour > 4 and hour < 12:
        speak('Good Morning!!')

    elif hour >= 12 and hour <= 16:
        speak('Good Afternoon!!')

    elif hour > 12 and hour <= 21:
        speak('Good Evening!!')
    else:
        speak('Good Night!!')
    speak("Please tell me how can I help you?")


# wishme()
