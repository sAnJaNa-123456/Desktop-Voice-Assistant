import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

# Function to take voice command
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# Function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to search on Google
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on Google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            speak("No speakable output available")

# Function to search on YouTube
def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

# Function to search on Wikipedia
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from Wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")

        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
            speak(f"No page matches the query '{query}'. Please try another query.")
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"The query '{query}' is ambiguous. Options: {e.options}")
        except wikipedia.exceptions.WikipediaException as e:
            speak(f"WikipediaException: {str(e)}")

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

# Example usage
query = takeCommand().lower()

if query:
    if "google" in query:
        searchGoogle(query)
    elif "youtube" in query:
        searchYoutube(query)
    elif "wikipedia" in query:
        searchWikipedia(query)
    else:
        speak("No query detected. Please try again.")
