# import speech_recognition as sr
import pyttsx3
# import pywhatkit
import wikipedia
import webbrowser as wb
import wikipedia as googleScrap

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


# def take_command():
#
#     """Recognizes the audio and sends it for display to displayText."""
#     # playsound.playsound("Mello_activation.wav")
#     r = sr.Recognizer()   # Speech recognition helps you to save time by speaking instead of typing.
#     # It helps us to communicate with our devices without writing one line of code
#
#     with sr.Microphone() as source:  # use the default microphone as the audio source
#         # speak.say('Hey I am Listening ')
#           print("Listening.......")
#           r.pause_threshold = 1
#           r.energy_threshold = 300
#           # speak.runAndWait()    # This function will make the speech audible in the system,
#           # if you don't write this command then the speech will not be audible to you
#           audio = r.listen(source, 0, 5)   # listen for the first phrase and extract it into audio data,
#         # wait for 5 seconds
#
#           try:
#               print('Recognizing....')
#               query = r.recognize_google(audio, language = 'en-US')
#               query = query.lower()
#               print(query)
#               # put = r.recognize_google(audio)
#
#           except Exception as e:
#               print(e)
#               speak("Please Say that again or check your internet connection!!")
#               return "None"
#     return query

# query = take_command().lower()


def searchGoogle(query):

    if "google" in query or 'search' in query:

        query = query.replace("google", '')
        query = query.replace("search", '')
        query = query.replace("google search", '')
        query = query.replace("on google", '')
        query = query.replace("please", "")
        query = query.replace("for me", "")
        query = query.replace("can you", "")
        speak('Searching')
        speak("This is what i found")
        try:
            # pywhatkit.search(query)
            result = googleScrap.summary(query, sentences = 1)
            print(result)
            speak(result)

        except:
            speak("Ohh No!!")
            speak("I am confused. Can you please try again!")
            quit()


def searchWikipedia (query):

    if 'wikipedia' in query:
        speak("searching")
        # finding result for the search
        # sentences = 2 refers to numbers of line
        query = query.replace('wikipedia', '')
        query = query.replace('search', '')
        query = query.replace('what is ', '')
        query = query.replace("please", "")
        query = query.replace("for me", "")
        query = query.replace("can you", "")
        reslt = wikipedia.summary(query, sentences=3)
        speak('According to the wikipedia')
        print(reslt)
        speak(reslt)
        quit()
