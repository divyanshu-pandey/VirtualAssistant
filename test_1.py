import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import subprocess
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from tkinter import *
import sys
import geocoder
from twilio.rest import Client


win=Tk()
win.title("Alfred")  
win.geometry("200x100")


def aw():
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[0].id)


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
    
        speak("I am Alfrid. Sir  Please tell me how may I help you")
    
    def takeCommand():
        #It takes microphone input from the user and returns string output
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
    
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('cptdishu@gmail.com', 'your-Dishu6161')
        server.sendmail('divyanshupandey434@gmail.com', to, content)
        server.close()
    
    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()
    
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
    
            elif 'open youtube' in query:
                speak("opening youtube")
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")
             
            elif 'close browser' in query:
                os.system("taskkill /im chrome.exe /f")
    
            elif 'open google' in query:
                speak("opening google")
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
            
    
            elif 'open stackoverflow' in query:
                speak("opening stackoverflow")
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("stackoverflow.com")
                
            elif 'open news' in query:
                speak("opening news for u")
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("ndtv.com")
                
            elif 'login my facebook' in query:
                speak("login your facebook account, Sir")
                username="9044026161"
                password="facebookwala1"
                url='https://www.facebook.com'
                driver=webdriver.Chrome()
                driver.get(url)
                driver.find_element_by_name('email').send_keys(username)
                driver.find_element_by_name('pass').send_keys(password)
                time.sleep(1)
                driver.find_element_by_id('loginbutton').click()
    
    
            elif 'play music' in query:
                speak("playing music")
                music_dir = 'C:/Users/dell/Music/Playlists'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            
            elif 'stop music' in query:
                os.system("taskkill /im vlc.exe /f")
                
                
    
            elif 'the time' in query: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
    
            elif 'open notepad' in query:
                speak("opening notepad")
                subprocess.run('C:\\Windows\\System32\\notepad.exe')
            elif 'close notepad' in query:
                os.system("taskkill /im notepad.exe /f")
                
           
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            
            elif 'current' in query:
                with requests.Session() as s:
                    speak("opening website")
                    url='https://www.worldometers.info/coronavirus/country/india/'
                    driver=webdriver.Chrome()
                    driver.get(url)
                    url=" https://www.worldometers.info/coronavirus/country/india/"
                    r= s.get(url)
                    soup=BeautifulSoup(r.content,"lxml")
                    current_status=soup.find(class_="maincounter-number")
                    cs=current_status.text
                    print(cs)
                    speak(f"current cases in india of corona are")
                    speak(cs)
                    
            elif 'emergency' in query:
                g = geocoder.ip('me')
                geo_loc=g.latlng
                geo_loc2= ' '.join(map(str,geo_loc))
    
                acc="AC860a77e25b4a312abc7c080f3492d6f4"
                token="133db6f4fa971b253b5311195d254ec5"
                client=Client(acc,token)

                client.messages.create(
                to="+919044026161",from_="+12029462150",body="it's Divyanshu .This is a  medical emergency. Contact me my location quardinates are:  "+geo_loc2)
    
                speak("ok sir, Sending emergency signal ")
                
            elif 'leave me alone' in query:
                speak("ok sir as your wish")
                speak(" it was fun to assist you")
                time.sleep(2)
                sys.exit()
            
                
            
                

button= Button(win,text="Launch Alfred", command=aw)
button.grid(row=1,column=0)
button.pack(pady=27)

win.mainloop()

