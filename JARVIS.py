import os
# import subprocess
import pyautogui
import pyttsx3   # pyttsx3 is a text-to-speech conversion library in Python
import datetime
import time
import requests
# import playsound
import speech_recognition as sr
# import wikipedia  # Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia
import webbrowser as wb  # Used for searching something in browser
import psutil   # Used for the details of device
import pyjokes  # Pyhton module which contains lots of jokes
from bs4 import BeautifulSoup
import wolframalpha
from plyer import notification
from pygame import mixer
import speedtest


for i in range(3):
    pas = input("Enter the password\n")
    file_read = open('psw.txt', 'r')
    mello_key = file_read.read()
    file_read.close()
    if pas == mello_key:
        print("WELCOME SWYAM! PLEASE SPEAK THAT MAGICAL WORD TO ACTIVATE YOUR ASSISTANT\n")
        break
    elif pas != mello_key:
        print('Try Again!!')
    elif i == 2 and pas != mello_key:
        exit()


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


def time_():

    """This function will provide the current time if user ask for the time !!"""

    tim = datetime.datetime.now().strftime('%I:%M %p')  # I = hour, M = minutes, p = PM; H = 24 hours clock
    # strftime is used to convert the time in string!!!
    speak('The current time is :')
    # print(tim)
    speak(tim)
    week_day = datetime.datetime.now().strftime('%A')
    speak('Today is:')
    speak(week_day)
    # print(week_day)


def date_():

    """This function will provide the today's date, if the user ask for date"""

    dat = datetime.datetime.now().strftime("%b %d, %Y")
    speak("Today's date is :")
    speak(dat)
    # print(dat)


def battery():

    """This function will provide all the details about your device battery!!"""

    batt = psutil.sensors_battery()  # Battery percentage !
    battery_percentage = str(batt.percent)
    charging = batt.power_plugged  # Will tell whether the device is under charging or not
    speak('Your device battery is at' + battery_percentage + 'percent')

    if int(battery_percentage) < 20 and not charging:  # This will remind about the battery of your device and also tell
        # how much battery time is left....
        speak('Please! Charge your device!')
        seconds = batt.secsleft  # Battery time which has been converted into hours, minutes and seconds!!
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        tim = "%d:%02d:%02d" % (hours, minutes, seconds)
        speak('Your battery will dead after {} hour {} minutes and {} seconds'.format(hours, minutes, seconds))
        print('Your battery will dead after {}'.format(tim))


def cpu():
    """This will tell the detail of the cpu"""
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)


def memory():

    """This function will tell the usage of memory!!"""

    mem_usage = psutil.virtual_memory()
    total = "{:.1f}".format(mem_usage.total / (1024 ** 3))
    used = "{:.1f}".format(mem_usage.used / (1024 ** 3))

    speak("You have total of {}GB of memory".format(total))
    time.sleep(1)
    speak("In which you have used {}GB".format(used))


def jokes():

    """This function will tell a joke!!!"""

    speak(pyjokes.get_joke())


def alarm(s):
        timewhere = open('Alarmtext.txt', 'a')
        timewhere.write(s)
        timewhere.close()
        os.startfile('Alarm.py')


def screenshot():
    my_screenshot = pyautogui.screenshot()
    tim = datetime.datetime.now().strftime("%I%M%d%m")
    path = "screenshot\\{}ss.png".format(tim)
    my_screenshot.save(path)
    speak('Done Swyam')

def wolframAlpha(query):
    api_key = '4QA4V3-L3HT3H2EE7'
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        print(next(requested.results).text)
        answer = next(requested.results).text
        return answer
    except:
        speak('The value is not answerable')


if __name__ == '__main__':
    """This is the main function which controls all the functions!"""

    while True:

        query = take_command()  # Takes the input form the user.

        if "hey mellow" in query or "ok mellow" in query or "ok milo" in query or "hey" in query or "milo" in query\
                or "hay" in query or "mellow" in query or "melo" in query or "malo" in query or "mello" in query or 'ok' in query:
            from greet_me import wishme
            wishme()

            while True:
                query = take_command().lower()
                if "go to sleep" in query or 'sleep' in query or "offline" in query or 'thank you' in query \
                        or 'thanks' in query:
                    speak("Ok sir, you can call me anytime!")
                    break

                elif "hello" in query:
                    speak("Hello sir, How are you??")

                elif "i am fine" in query or "i am good" in query:
                    speak("that's great sir!!!")
                    speak("Tell me how can i help you ??")

                elif "how are you" in query or "how's you" in query or "how you doing" in query or "kaise ho" in query:
                    speak("I am fantastic, What about you??")

                elif 'who are you' in query or 'introduction' in query or 'introduce' in query:
                    speak("So, I am a project which has been initiated by swyam in his fourth year of Btech, "
                          "Swyam made me with the help of Python and libraries, I also co-operate with everyone.")
                    speak('If you want to know more about swyam, I am providing you his Linkedin profile, '
                          'so as git hub profile')
                    wb.open_new_tab('https://www.linkedin.com/in/swyam-srivastava-b789521b0?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BA29UL3QpTdumvgfbqAI4rw%3D%3D')
                    wb.open_new_tab('https://github.com/swyamsrv')
                    time.sleep(10)
                    # speak("How can i help you sir?")
                    speak('Anything else sir?')

                elif 'i love you' in query or 'love you' in query:
                    speak('I also love you, But I am not a human like you')

                elif 'what are you doing' in query or 'kar rhe ho' in query:
                    speak('I am doing my task to help, swyam in his daily routine')

                elif 'not good' in query or 'not feeling good' in query or 'not feeling well' in query or 'i am sad' in query:
                    speak("That's not good, Let me chill your mood by some jokes\n")
                    jokes()

                elif 'time' in query:
                    time_()  # will provide the time to the user!!

                elif 'date' in query:
                    date_()  # Will gives provide the time to the user

                elif 'goto sleep' in query or 'go to sleep' in query:
                    speak('Ok sir, You can call me anytime!')

                elif 'what is' in query or 'who is' in query:
                    query = query.replace('what is ', '')
                    query = query.replace('who is', '')
                    query = query.replace('answer', '')
                    ans = str(wolframAlpha(query))
                    speak(ans)

                elif 'change password' in query or 'change my password' in query:
                    speak('Enter your current password')
                    pas = input("Enter your current password\n")
                    file_read = open('psw.txt', 'r')
                    mello_key = file_read.read()
                    file_read.close()
                    if pas == mello_key:
                        speak("Please enter your new password")
                        new_pass = input("Enter your new password\n")
                        file_read = open('psw.txt', 'w')
                        file_read.write(new_pass)
                        file_read.close()
                        speak('Password updated successfully')
                    elif pas != mello_key:
                        speak('You have entered wrong password')
                        exit()

                # elif 'wikipedia' in query:
                #     speak('Searching')
                #     # finding result for the search
                #     # sentences = 2 refers to numbers of line
                #     query = query.replace('wikipedia', '')
                #     result = wikipedia.summary(query, sentences = 3)
                #     speak('According to the wikipedia')
                #     print(result)
                #     speak(result)

                elif 'on chrome' in query or 'open chrome' in query:
                    speak('What should i search??')
                    chrome = take_command()
                    speak("Opening Chrome")
                    wb.open_new_tab('https://www.google.com/search?q=' + chrome)

                elif 'in youtube' in query or 'on youtube' in query or 'in you tube' in query or 'youtube' in query \
            or 'open you tube' in query or 'open youtube' in query:
                    speak('What should i search?')
                    youtube = take_command()
                    if youtube == 'None':
                        youtube = take_command()
                    speak('Opening You tube !')
                    wb.open('http://www.youtube.com/results?search_query=' + youtube)
                    break

                elif 'open' in query:
                    if ".com" in query or ".co.in" in query or ".org" in query:
                        from open_app import openweb
                        openweb(query)
                    else:
                        from open_app import default_app
                        default_app(query)

                elif "google" in query or 'search' in query:
                    from search_now import searchGoogle
                    searchGoogle(query)

                elif "wikipedia" in query:
                    from search_now import searchWikipedia
                    searchWikipedia(query)

                elif 'in chrome' in query or 'on chrome' in query:
                    speak('what should i search?')
                    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    search = take_command()
                    wb.get(chromepath).open_new_tab(search+'.com')

                elif 'battery' in query or 'battery percentage' in query:
                    battery()

                elif 'memory' in query or 'memory usage' in query:
                    memory()

                elif 'cpu' in query or 'cpu usage' in query:
                    cpu()

                elif 'joke' in query:
                    jokes()

                if 'bye' in query or 'good night' in query or 'Stop listening' in query or 'we are done' in query \
                        or 'i am done' in query:
                    speak('Okay so you are leaving, Swyam')
                    speak('Hope you will call me again!')
                    quit()

                elif 'temperature' in query or 'weather' in query:
                    search = "Temperature in Lucknow"
                    url = "https://www.google.com/search?q={}".format(search)
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak("Current Temperature in Lucknow is {}".format(temp))

                elif 'set an alarm' in query or 'alarm' in query:
                    print('Enter the time in hh:mm in 12 HOURS CLOCK \n')
                    speak('Set the time')
                    h, m = map(str, input().split())
                    a = "{}:{}:00".format(h, m)
                    alarm(a)
                    speak('Done, Swyam')
                    speak('Alarm has been set for {}:{}'.format(h, m))
                    quit()

                elif 'remember that' in query:
                    remeberMsg = query.replace('remember that', '')
                    remeberMsg = remeberMsg.replace('Please', '')
                    speak('You told me '+remeberMsg)
                    remember = open('Remember.txt', 'w')
                    remember.write(remeberMsg)
                    remember.close()

                elif 'what do you remember' in query or 'do you remember' in query:
                    remember = open('Remember.txt', 'r')
                    speak('You told me ' + remember.read())
                    remember.close()

                elif 'news' in query or 'latest updates' in query :
                    from newsread import latest_news
                    latest_news()

                elif 'translate' in query:
                    from translator import translate
                    query = query.replace('please', '')
                    query = query.replace('transalte', '')
                    translate(query)

                elif 'calculate' in query or '+' in query or '-' in query or 'into' in query or 'plus' in query \
                        or 'minus' in query:
                    from calculatenum import wolframAlpha
                    from calculatenum import calc
                    query = query.replace('calculate', '')
                    query = query.replace('what will be the answer of', '')
                    query = query.replace('please', '')
                    query = query.replace('answer', '')
                    wolframAlpha(query)
                    calc(query)

                elif 'whatsapp' in query or 'whatsapp message' in query:
                    from WA import sendMessage
                    sendMessage()

                elif 'shutdown' in query or 'shut down' in query:
                    speak("Are you sure, you wanna shutdown your computer?")
                    speak('Say yes or no')
                    inpt = take_command()
                    if inpt == 'yes':
                        os.system('shutdown /s /t 1')
                    else:
                        speak('ok shutdown canceled')
                        break

                elif 'restart' in query:
                    speak("Are you sure, you want to restart your computer? ")
                    speak('Say yes or no')
                    inpt = take_command()
                    if inpt == 'yes':
                        os.system('shutdown /r /t 1')
                    else:
                        speak('ok restart canceled')
                        break

                elif 'show my schedule' in query:
                    file = open("task.txt", 'r')
                    content = file.read()
                    file.close()
                    time.sleep(2)
                    mixer.init()
                    mixer.music.load('task_notifier.mp3')
                    mixer.music.play()
                    notification.notify(
                        title="My schedule",
                        message=content,
                        timeout=15
                    )

                elif "schedule" in query:
                    tasks = []  # EMPTY LIST FOR STORING TASK
                    speak("Do you want to clear old task")
                    speak('Speak yes or no')
                    usr = take_command().lower()
                    if 'yes' in usr:
                        file = open('task.txt', 'w')
                        file.write('')
                        file.close()
                        speak('Please wait')
                        time.sleep(4)
                        speak("How many task do you want to add?")
                        no_of_task = take_command()
                        while no_of_task.isalpha() or not no_of_task.isdigit():
                            no_of_task = take_command()
                            break
                        i = 0
                        for i in range(int(no_of_task)):
                            speak("Tell your task")
                            tasks.append(take_command())
                            file = open('task.txt', 'a')
                            file.write('\n{}'.format(tasks[i]))
                            file.close()
                    elif 'no' in usr:
                        speak("How many task do you want to add?")
                        no_of_task = take_command()
                        while no_of_task.isalpha() or not no_of_task.isdigit():
                            no_of_task = take_command()
                            break
                        i = 0
                        for i in range(int(no_of_task)):
                            speak("Tell your task")
                            tasks.append(take_command())
                            file = open('task.txt', 'a')
                            file.write('\n{}'.format(tasks[i]))
                            file.close()

                elif 'internet speed' in query:
                    speak('Please wait, Swyam')
                    wifi = speedtest.Speedtest()
                    download_speed = wifi.download()/1024**2
                    print("Your Download speed is {:.1f} MB".format(download_speed))
                    speak("Your Download speed is {:.1f} MB".format(download_speed))
                    upload_speed = wifi.upload()/1024**2
                    print("Your Upload speed is {:.1f} MB".format(upload_speed))
                    speak("Your Upload speed is {:.1f} MB".format(upload_speed))

                elif 'write a note' in query:
                    speak("What should i write, Swyam?")
                    notes = take_command()
                    file = open('notes.txt', 'w')
                    strTime = datetime.datetime.now().strftime("%I:%M:%S")
                    file.write(strTime)
                    file.write(':-')
                    file.write(notes)
                    speak('Done taking notes, Swyam!!')

                elif 'show my notes' in query:
                    speak('showing notes')
                    file = open('notes.txt', 'r')
                    print(file.read())

                elif 'screenshot' in query or 'screen shot' in query:
                    screenshot()

                elif 'take my photo' in query:
                    speak('Ok swyam')
                    speak('Please wait')
                    os.system('start microsoft.windows.camera:')
                    time.sleep(5)
                    speak('Smile')
                    pyautogui.press('enter')

                elif 'where is' in query:
                    query = query.replace('where is', '')
                    query = query.replace('direct me to', '')
                    query = query.replace('what is the location of', '')
                    query = query.replace('locate me', '')
                    location = query
                    speak('Please wait')
                    time.sleep(2)
                    speak("You asked to locate " + location)
                    wb.open_new_tab('https://www.google.com/maps/place/{}'.format(location))





