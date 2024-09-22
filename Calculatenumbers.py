import wolframalpha
import pyttsx3
import speech_recognition


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "YR77TA-V46JXH2WEJ"  # Replace with your Wolfram Alpha API key
    requester = wolframalpha.Client(apikey)
    
    try:
        requested = requester.query(query)
        answer = next(requested.results).text
        return answer
    except StopIteration:
        speak("I'm sorry, I couldn't find an answer.")
    except Exception as e:
        print(f"Error querying Wolfram Alpha: {e}")
        speak("There was an issue processing your request.")

def Calc(query):
    # Replace specific words with mathematical operators
    Term = query.lower()
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    try:
        result = WolfRamAlpha(Term)
        if result:
            print(f"Result: {result}")
            speak(f"The result is {result}")
        else:
            speak("The result is not available.")
    except Exception as e:
        print(f"Error calculating: {e}")
        speak("There was an issue calculating the result.")