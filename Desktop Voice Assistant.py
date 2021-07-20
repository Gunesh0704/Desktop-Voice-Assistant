import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import pyjokes
import urlopen
import json
import wolframalpha

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
         speak("Good Evening!")  

    speak("I am Virtual. Sir,Please tell me how may I help you")  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
 
        print("Say that Again Please")
        return"None"
    return query      

if __name__ == '__main__':
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #Logic for Executing task on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://google.com")
            
        elif 'open Translate' in query:
            speak("Here you go to Google Translate\n")
            webbrowser.open("https://translate.google.co.in/")    
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://stackoverflow.com")  
 
        elif 'play music' in query or 'play songs' in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\MOHANE HOAME\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[0]))
 
        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'Open VS code' in query:
            codePath = "C:\\Users\\MOHANE HOAME\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Ayush Mohane.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif "calculate" in query:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Ayush Mohane. further It's a secret")


        elif "who are you" in query:
            speak("I am your virtual assistant created by Ayush Mohane")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Ayush Mohane ")


        elif 'Tell me news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))    


 