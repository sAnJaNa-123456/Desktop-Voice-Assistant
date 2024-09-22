import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e2a469267e9649d19eab244ddbb80f20",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e2a469267e9649d19eab244ddbb80f20",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e2a469267e9649d19eab244ddbb80f20",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e2a469267e9649d19eab244ddbb80f20",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e2a469267e9649d19eab244ddbb80f20"
    }

    url = None
    speak("Which field news do you want, [health], [technology], [sports], [entertainment], [science]")
    field = input("Type field news that you want: ")
    
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("URL found")
            break
    
    if url is None:
        speak("Sorry, I couldn't find news for that category.")
        return
    
    try:
        news = requests.get(url).text
        news = json.loads(news)
        speak("Here is the first news.")
    
        articles = news["articles"]
        for article in articles:
            title = article["title"]
            print(title)
            speak(title)
            news_url = article["url"]
            print(f"For more info visit: {news_url}")
    
            choice = input("[Press 1 to continue] or [Press 2 to stop]: ")
            if choice == "1":
                continue
            elif choice == "2":
                break
    
        speak("That's all for now.")
    
    except requests.exceptions.RequestException as e:
        speak("Sorry, there was an error fetching the news. Please try again later.")
        print(f"Error: {e}")

# Example usage
latestnews()
