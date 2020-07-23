import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

 
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<8:
        speak("Good Morning! get up and gym make those muscles flex")
    
    if hour>=8 and hour<12:
        speak("How is your morning tanya?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    elif hour>=18 and hour<=22:
        speak("Good Evening!")
    else:
        speak("Tanya,that was a long day, time for a nap.zzz")

    speak("I am Potter mam. at your command")   

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:   
        print("Say that again please...")   
        return "None" 
    return query

 

if __name__=="__main__" :
    wishme()
    while True:
   
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeks for geeks.com")
        
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        
        elif ' open Linkedin' in query:
            webbrowser.open("Linkedin.com")

        elif 'open mails' in query:
            webbrowser.open("gmail.com")

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        elif 'open vs code' in query:
            codePath="C:\\Users\\tanya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'i love you potter' in query:
            speak("i love you too dear tanya, you are the best")
        
        elif 'who are my best friend' in query:
            speak("Mehak,ayushi,aditi,payal,sweety are you friends")

        elif 'what is the purpose of life' in query:
            speak("finding happiness is the purpose of life")

        elif'when is my birthday' in query:
            speak("wohhooo!!  Your birthday is on 29th February")

        elif'how are you potter' in query:
            speak("I am always fabulous Tanya.how about you?")

        elif'who is my sister' in query:
            speak("Somya Charan Pahadi is your sister") 

        elif 'bye bye potter' in query:
           os._exit(0)

