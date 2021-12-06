# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:22:55 2021

@author: ASUS
"""
import pyttsx3
#import smtplib
#import os
#import pyaudio
import cv2
#import subprocess
import datetime
import webbrowser
import speech_recognition as ani
from time import ctime
import pyjokes

gs=ani.Recognizer()
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def record():
    
    with ani.Microphone() as inp:
         print('listening....')
         out=gs.listen(inp)
         store = ''
         try:
             print('Recognizing...')
             store = gs.recognize_google(out)
             print(store)
         except ani.UnknownValueError:
            print('sorry didnt get that')
         except ani.RequestError:
          print('service error')
            
    return store

            
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour >=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    print('What should i call you sir?')
    speak('what should i call you sir?') 
    name=record().lower()
    print('Hello '+name+ 'I I am Arya')
    speak ('hello '+ name +" I am aarya")
    print("How can i help you?")
    speak("How can i help you?")


def respond(store):
    
    if 'what is your name' in store:
        print('my name is Lilli')
        speak('my name is LIlli')
        
    elif 'time' in store:
        print(ctime())
        speak(ctime())
        
    elif 'hey good morning' in store:
        print('Good morning sir.')
        speak('Good morning sir.')
        
    elif 'good evening' in store:
        print('Good Evening sir.')
        speak('Good Evening sir.')
        
    elif 'good night arya' in store:
        print('Good Night Sweet Dreams...')
        speak('Good Night Sweet Dreams...')
        
    elif 'open youtube' in store:
        print('you are redirecting to youtube')
        speak('you are redirecting to youtube')
        webbrowser.open("youtube.com")
        
    elif 'open google' in store:
        print('You were redirecting to google')
        speak('opening google')
        webbrowser.open("google.com")
        
    elif 'search' in store:
        print('What you want to search')
        speak('what you want to search')
        query=record().lower()
        webbrowser.open("https://www.google.co.in/search?q=" + query)
        
    elif "take" and "photo" and "picture" in store:
       while 1:
           vid=cv2.VideoCapture(0)
           ret, frame= vid.read()
           cv2.imshow('frame', frame)    
            
           if cv2.waitKey(1) & 0xFF==ord("E"):
               break
          
       vid.release()
       cv2.destroyAllWindows()
            
    elif 'play video on youtube' in store:
        print('Name of the video you want to play')
        speak('name of the video you want to play')
        query=record().lower()
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)
        
    elif 'play music' in store:
        print('Name the platform where you want to listen')
        speak('name the platform where you want to listen')
        
        say=record().lower()
        if 'spotify' in say:        
            print('Name of the song you want to play')
            speak('name of the song you want to play')
            query=record().lower()
            webbrowser.open("https://open.spotify.com/search/" + query)
            
        elif 'jio saavan' in say:
            print('Name of the song you want to play')
            speak('name of the song you want to play')
            query=record().lower()
            webbrowser.open("https://www.jiosaavn.com/search/" + query)
            
        elif 'gana' in say:
            print('Name of the song you want to play')
            speak('name of the song you want to play')
            query=record().lower()
            webbrowser.open("https://gaana.com/search/" + query)
    elif 'jokes' in store:
        joke=pyjokes.get_joke(language='en', category='all')
        print(joke)
        speak(joke)
        
    elif 'open lpu live' in store:
        print('you are redirecting to LPU LIVE')
        speak('you are redirecting to LPU LIVE')
        webbrowser.open("lpulive.lpu.in")

    elif 'open o a s' in store:
        print('you are redirecting to OAS')
        speak('you are redirecting to OAS')
        webbrowser.open("oas.lpu.in/")

    elif 'open u m s' in store:
        print('you are redirecting to UMS')
        speak('you are redirecting to UMS')
        webbrowser.open("ums.lpu.in/lpuums/")

    elif 'open my class' in store:
        print('you are redirecting to My Class')
        speak('you are redirecting to My Class')
        webbrowser.open("myclass.lpu.in/")  

greet()
store = record().lower()
respond(store)
