import wolframalpha
import pyttsx3
import speech_recognition as sr

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
    # playsound.playsound("Mello_activation.wav")
    r = sr.Recognizer()   # Speech recognition helps you to save time by speaking instead of typing.
    # It helps us to communicate with our devices without writing one line of code

    with sr.Microphone() as source:  # use the default microphone as the audio source
        # speak.say('Hey I am Listening ')
          print("Listening.......")
          r.pause_threshold = 1
          r.energy_threshold = 300
          # speak.runAndWait()    # This function will make the speech audible in the system,
          # if you don't write this command then the speech will not be audible to you
          audio = r.listen(source, 0, 4)   # listen for the first phrase and extract it into audio data,
        # wait for 5 seconds

def wolframAlpha(query):
    api_key = '4QA4V3-L3HT3H2EE7'
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak('The value is not answerable')

def calc(query):
    term = str(query)
    term = term.replace('please', '')
    term = term.replace('answer', '')
    term = term.replace('multiply', '*')
    term = term.replace('into', '*')
    term = term.replace('divide', '/')
    term = term.replace('upon', '/')
    term = term.replace('add', '+')
    term = term.replace('plus', '+')
    term = term.replace('subtract', '-')
    term = term.replace('minus', '-')

    final = str(term)
    try:
        result = wolframAlpha(final)
        print("{}".format(result))
        speak(result)
    except:
        speak('The value is not answerable')