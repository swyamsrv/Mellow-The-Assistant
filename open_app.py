# import pyautogui
import webbrowser
import pyttsx3
import subprocess
import os
import webbrowser as wb
"""Subprocess in Python is a module used to run new codes and applications by creating new processes. It lets you 
# start new applications right from the Python program you are currently writing."""


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


def openweb(query):
    speak("Opening")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("search", "")
        query = query.replace("please", "")
        query = query.replace("for me", "")
        query = query.replace("can you", "")
        query = query.replace(" ", "")  # If space in query
        query = query.replace("goto" or "go to" , "")
        webbrowser.open("https://www.{}".format(query))

def default_app(query):
    if "anaconda" in query:
        speak("Opening Anaconda Navigator")
        subprocess.Popen("C:\\ProgramData\\Anaconda3\\pythonw.exe C:\\ProgramData\\Anaconda3\\cwp.py C:\\ProgramData\\Anaconda3 C:\\ProgramData\\Anaconda3\\pythonw.exe C:\\ProgramData\\Anaconda3\\Scripts\\anaconda-navigator-script.py")
        # os.system('start anaconda')......
    elif "data studio" in query:
        speak("Opening Azure data studio")
        subprocess.Popen("C:\\Program Files\\Azure Data Studio\\azuredatastudio.exe")
    elif "blue stack" in query or 'bluestack' in query:
        speak("opening blue stack")
        subprocess.Popen("C:\Program Files (x86)\BlueStacks X\BlueStacks X.exe")
    elif "open camera" in query:
        speak("opening camera")
        os.system('start microsoft.windows.camera:')
    elif "calculator" in query:
        speak("opening calculator")
        os.system("start calc")
        # subprocess.Popen('C:\\Windows\\System32\\calc.exe')....
    elif "control panel" in query:
        speak("opening control panel")
        os.system('start Control Panel')
    elif "command prompt" in query or "cmd" in query:
        speak('opening command prompt')
        os.system("start cmd")
    elif "excel" in query:
        speak('opening Microsoft excel')
        os.system('start excel')
    elif 'edge' in query:
        speak("opening Microsoft edge")
        os.system('start msedge')
    elif 'file' in query or 'file explorer' in query or 'files' in query:
        speak('opening file explorer')
        os.system('start explorer')
    elif 'open google chrome' in query:
        speak('opening google chrome')
        os.system('start chrome')
    elif 'github' in query or 'git hub' in query:
        speak("opening git hub desktop")
        subprocess.Popen("C:\\Users\\swyam\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
    elif 'instagram' in query or 'insta' in query:
        speak("opening instagram")
        wb.open_new_tab("https://instagram.com")
    elif 'jupiter notebook' in query or 'jupiter' in query or 'jupyter' in query:
        speak('Opening jupyter notebook')
        subprocess.Popen("C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 "
                         "C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py")
    elif 'open map' in query:
        speak("opening google map")
        wb.open_new_tab("https://www.google.com/maps/@21.125498,81.914063,5z")
    elif 'media player' in query:
        speak('opening windows media player')
        os.system('start wmplayer')
    elif 'open mail' in query or 'open male' in query or 'open gmail' in query:
        speak('opening g mail')
        wb.open_new_tab('https://mail.google.com')
    elif 'microsoft store' in query:
        speak('opening microsoft store')
    elif 'on screen keyboard' in query or 'onscreen keyboard' in query:
        speak('opening keyboard on your screen')
        # subprocess.Popen('C:\\Users\\swyam\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\%windir%\\'
        #                  'system32\\osk.exe')
        os.system('start osk')
    elif 'teams' in query:
        speak('opening microsoft teams')
        os.system('start msteams')
    elif 'notepad' in query:
        speak('opening notepad')
        os.system('start notepad')
    elif 'one drive' in query or 'onedrive' in query:
        speak('opening one drive')
        subprocess.Popen("C:\\Program Files\\Microsoft OneDrive\\OneDrive.exe")
    elif 'one note' in query or 'onenote' in query:
        speak("opening one note")
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")
    elif 'python' in query:
        speak('opening Python')
        os.system('start python')
    elif 'pycharm' in query or 'py charm' in query or 'python' in query:
        speak('opening pycharm, a python I D L E')
        subprocess.Popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.1\\bin\\pycharm64.exe")
    elif 'paint' in query:
        speak('opening paint')
        os.system('start mspaint')
    elif 'power bi' in query or 'powerbi' in query or 'power b i ' in query:
        speak('opening power b i')
        subprocess.Popen("C:\\Program Files\\Microsoft Power BI Desktop\\bin\\PBIDesktop.exe")
    elif 'power point' in query or 'powerpoint' in query:
        speak("opening microsoft power point")
        os.system('start powerpnt')
    elif 'settings' in query or 'setting' in query:
        speak('opening settings')
        os.system('start ms-settings:')
    elif 'system information' in query:
        speak('open system information')
        os.system('msinfo32')
    elif "telegram" in query:
        speak('opening telegram')
        os.system("start Telegram")
    elif 'visual studio' in query or 'vs code' in query or 'visual' in query or 'vs studio' in query:
        speak('opening visual studio code')
        subprocess.Popen("C:\\Users\\swyam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif 'word' in query or 'microsoft word' in query:
        speak('opening Mircosoft word')
        os.system('start winword')
    elif 'whatsapp' in query or 'whats app' in query:
        speak('opening whatsapp')
        wb.open_new_tab('https://web.whatsapp.com/')
    elif 'zoom' in query:
        speak('opening zoom')
        subprocess.Popen("C:\\Users\\swyam\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    else:
        query = query.replace("open", "")
        query = query.replace("please", "")
        query = query.replace(" ", '')
        query = query.replace("for me", "")
        query = query.replace("search", "")
        speak('opening {}'.format(query))
        wb.open_new_tab("https://www.{}.com".format(query))





