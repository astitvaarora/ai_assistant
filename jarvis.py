import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir')
    
    else:
        speak('Good Evening sir')
    
    speak("this is your Ai assistant Jarvis how can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query    

        
if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        # logic for executing tasks based on query
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)
            speak('accouding to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open('youtube.com') 

        elif 'open google' in query:
            webbrowser.get(chrome_path).open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open('stackoverflow.com')

        elif 'open github' in query:
            webbrowser.get(chrome_path).open('github.com')    

        elif 'open facebook' in query:
            webbrowser.get(chrome_path).open('facebook.com')
        elif 'play' in query:
            pywhatkit.playonyt(query)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {strTime}") 
        elif "rap" in query:
            speak('''Just waking up in the morning gotta thank God
                    I don't know but today seems kinda odd
                    No barking from the dogs, no smog
                    And momma cooked a breakfast with no hog
                    I got my grub on, but didn't pig out
                    Finally got a call from a girl want to dig out
                    Hooked it up on later as I hit the do'
                    Thinking will i live another twenty fo'
                    I gotta go cause I got me a drop top
                    And if I hit the switch, I can make the ass drop
                    Had to stop at a red light
                    Looking in my mirror not a jacker in sight
                    And everything is alright
                    I got a beep from Kim and she can fuck all night
                    Called up the homies and I'm askin' y'all
                    Which park, are y'all playin' basketball?
                    Get me on the court and I'm trouble
                    Last week fucked around and got a triple double
                    Freaking brothers every way like M.J.
                    I can't believe, today was a good day''')
        elif 'story' in query:
            speak("once upon a time there was a boy abhinav")
        elif 'on google' in query:
            pywhatkit.search(query)
        elif 'shut down my computer' in query:
            pywhatkit.shutdown(time=20)
        elif 'open code' in query:
            path = "C:\\Users\\astitva\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(path)
