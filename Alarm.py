import pyttsx3
import datetime
import os
import time
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


extracted_time = open('Alarmtext.txt', 'rt')
time_ = extracted_time.read()
time_ = str(time_)
extracted_time.close()

delete_time = open('Alarmtext.txt', 'r+')
delete_time.truncate(0)
delete_time.close()

def ring(time_):
    timeset = str(time_)
    timenow = timeset.replace('set an alarm', " ")
    timenow = timenow.replace('please', "")
    timenow = timenow.replace('alarm', '')
    timenow = timenow.replace('can you', '')
    timenow = timenow.replace(' and ', '')
    timenow = timenow.replace('of', "")
    Alarmtime = str(timenow)
    while True:
        currenttime = datetime.datetime.now().strftime("%I:%M:%S")
        if currenttime == Alarmtime:
            speak('Alarm ringing, Swyam!!')
            os.startfile('alarm_minion.mp3')
        elif currenttime + '00:00:30' == Alarmtime:
            exit()
ring(time_)