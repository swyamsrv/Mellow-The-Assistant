import requests
import speech_recognition as sr
import json
import pyttsx3

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

          try:
              print('Recognizing....')
              query = r.recognize_google(audio, language = 'en-US')
              query = query.lower()
              print(query)
              # put = r.recognize_google(audio)

          except Exception as e:
              print(e)
              # speak("Please Say that again")
              return "None"
    return query


def latest_news():

    news_api = {'business' : 'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5589dcb45ac74ebc8a9db34725ec596d',
                'entertainment' :'https://newsapi.org/v2/top-headlines?country=in&apiKey=5589dcb45ac74ebc8a9db34725ec596d',
                'health': 'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=5589dcb45ac74ebc8a9db34725ec596d',
                'science' : 'https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=5589dcb45ac74ebc8a9db34725ec596d',
                'technology': 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5589dcb45ac74ebc8a9db34725ec596d',
                'sports' : 'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=5589dcb45ac74ebc8a9db34725ec596d'}

    content = None
    url = None
    speak('Which field news do you want?')
    speak('Business, Entertainment, Health, Science, Technology or Sports')
    speak('For example, if you want to listen Business related news just say business!')
    news_category = take_command()
    print(news_category)

    if news_category not in news_api.keys():
        speak('Please say that again\n')
        news_category = take_command()
        print(news_category)

    elif news_category in news_api.keys():
        url = news_api[news_category]
        print(url)
        speak('Please wait')
        print('please wait!')

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here's the first news.")
    article_news = news['articles']
    for articles in article_news:
        article = articles['title']
        print(article)
        speak(article)
        news_url = articles['url']
        speak('For more information click the link below')
        print('For more info visit:{}'.format(news_url))

        a = input('[Press 1 to continue] and [Press 2 to Stop]\n')
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break


