import datetime
import os
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import random
import webbrowser
from plyer import notification
from pygame import mixer
import time
import pyautogui
import pygetwindow as gw
import language_tool_python
import nltk
from nltk.corpus import wordnet
import requests
import speedtest
from googletrans import Translator


def download_nltk_resources():
    try:
        nltk.data.find('corpora/wordnet.zip')
    except LookupError:
        nltk.download('wordnet')
        nltk.download('omw-1.4')

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("WELCOME SIR! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif i == 2 and a != pw:
        exit()
    elif a != pw:
        print("Try Again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def check_internet():
    try:
        requests.get('https://www.google.com/', timeout=5)
        return True
    except requests.ConnectionError:
        return False
    
def check_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()
        download_speed = results["download"] / 1_000_000  
        upload_speed = results["upload"] / 1_000_000  
        ping = results["ping"]
        return f"Download speed: {download_speed:.2f} Mbps, Upload speed: {upload_speed:.2f} Mbps, Ping: {ping} ms"
    except Exception as e:
        return f"Error checking internet speed: {e}"
    
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def get_definition(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return "No definition found"

def maximize_window():
    window = gw.getActiveWindow()
    if window:
        window.maximize()
        speak("Window maximized")
    else:
        speak("No active window found")

def scroll_up():
    pyautogui.scroll(300)
    speak("Scrolled up")

def scroll_down():
    pyautogui.scroll(-300)
    speak("Scrolled down")

def zoom_in():
    pyautogui.keyDown('ctrl')
    pyautogui.press('+')
    pyautogui.keyUp('ctrl')
    speak("Zoomed in")

def zoom_out():
    pyautogui.keyDown('ctrl')
    pyautogui.press('-')
    pyautogui.keyUp('ctrl')
    speak("Zoomed out")

def refresh_screen():
    pyautogui.press('f5')
    speak("Screen refreshed")

def save_file():
    pyautogui.hotkey('ctrl', 's')
    speak("File saved")

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text, matches


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("You are welcome, sir")

                elif "open" in query:
                    query = query.replace("open", "").strip()
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "zoom in" in query:
                    zoom_in()

                elif "zoom out" in query:
                    zoom_out()

                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    songs = [
                        "https://www.youtube.com/watch?v=O5gwxm3NxFU",
                        "https://www.youtube.com/watch?v=0Iu5kQi8lns",
                        "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
                    ]
                    webbrowser.open(random.choice(songs))

                elif "define" in query:
                    word = query.replace("define", "").strip()
                    definition = get_definition(word)
                    speak(f"The definition of {word} is: {definition}")
                    print(f"Definition of {word}: {definition}")

                elif "change password" in query:
                    speak("What's the new password?")
                    new_pw = input("Enter the new password\n")
                    with open("password.txt", "w") as new_password:
                        new_password.write(new_pw)
                    speak("Done sir. Your new password is set.")

                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                    speak("Screenshot taken")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "maximize" in query:
                    maximize_window()

                elif "scroll up" in query:
                    scroll_up()

                elif "scroll down" in query:
                    scroll_down()

                elif "refresh the screen" in query:
                    refresh_screen()

                elif "save the file" in query:
                    save_file()

                elif "check grammar" in query:
                    speak("Please enter the text you want to check for grammatical errors:")
                    text = input("Enter the text: ")
                    corrected_text, matches = check_grammar(text)
                    if matches:
                        speak("The corrected text is:")
                        speak(corrected_text)
                        print("Corrected Text:", corrected_text)
                        for match in matches:
                            print(match)
                    else:
                        speak("No grammatical errors found.")

                elif "check internet speed" in query:
                    if check_internet():
                        internet_speed = check_internet_speed()
                        speak(internet_speed)
                        print(internet_speed)
                    else:
                        speak("Internet connection is not available.")                    

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    query = query.replace("calculate", "").strip()
                    try:
                        result = eval(query)
                        speak(f"The result of {query} is {result}")
                    except Exception as e:
                        speak("Sorry, I couldn't calculate that.")

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "temperature" in query:
                    search = "temperature in hyderabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "weather" in query:
                    search = "weather in hyderabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "the date" in query:
                    strDate = datetime.datetime.now().strftime("%B %d, %Y")
                    speak(f"Sir, today's date is {strDate}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "translate" in query:
                    parts = query.split("translate")
                    if len(parts) > 1:
                        text_to_translate = parts[1].strip()
                        target_language = "fr"  # Default target language (French), change as needed
                        translated_text = translate_text(text_to_translate, target_language)
                        speak(f"The translation of '{text_to_translate}' in {target_language} is: {translated_text}")
                        print(f"Translation: {translated_text}")
                    else:
                        speak("Please provide text to translate and target language")

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").strip()
                    speak("You told me to remember that " + rememberMessage)
                    with open("Remember.txt", "a") as remember:
                        remember.write(rememberMessage + "\n")

                elif "what do you remember" in query:
                    with open("Remember.txt", "r") as remember:
                        content = remember.read()
                        if content.strip():
                            speak("You told me to remember: " + content)
                        else:
                            speak("I don't seem to remember anything right now.")

                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()

                elif "restart the system" in query:
                    speak("Are you sure you want to restart?")
                    restart = input("Do you wish to restart your computer? (yes/no) ")
                    if restart.lower() == "yes":
                        os.system("shutdown /r /t 1")
                    elif restart.lower() == "no":
                        speak("Restart cancelled")

                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdown?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no) ")
                    if shutdown.lower() == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown.lower() == "no":
                        speak("Shutdown cancelled")

            


                
