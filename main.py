import speech_recognition as sr
import pyttsx3
import time
#import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import tkinter
from tkinter import *
from PIL import ImageTk,Image
import subprocess
import json
import requests
import wikipedia as wk
import time
import re

t = time.asctime().split(" ")
t2 = t[3].split(":")
tt1 = (t2[0])
print(tt1)
t1 = int(tt1)
print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()

def record_audio(ask= False ):
    with sr.Microphone() as source:
      if  ask:
            lee_voice(ask)
      audio = r.listen(source, phrase_time_limit = 3) 
      voice_data = ''
      try:
        voice_data = r.recognize_google(audio)
        print('Recognizer voice :' + voice_data)


      except Exception:
          print('Oops something went Wrong')
      return voice_data

def lee_voice(audio_string):

  tts = gTTS(text=audio_string, lang='en')
  r =random.randint(1, 1000000)

  audio_file = 'audio-' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  #tts.remove(audio_file)
  os.remove(audio_file)



class Widget:
  def __init__(self):
      root=Tk()
      root.geometry('1360x768')
      load=Image.open('carbgf.jpg')
      rend=ImageTk.PhotoImage(load)
      img=Label(root,image=rend)
      img.place(x=0, y=0)
      root.title("Drivers Virtual Assistant")
      lab1 = Label(root, text="Driver's Virtual Assistant", font=("agency FB", 70, 'bold'), fg='#883935',bg='#1A1112', activebackground='#1A1112').pack(side='top', pady=30)
      img = Image.open('gmic1.jpg')
      b = ImageTk.PhotoImage(img.resize((25,49)))
      lab2 = Label(root, image = b)
      lab2.place(x=500,y=480)
      img1 = PhotoImage(file='spkb.png')
      b2= Button(root, image=img1, bg='black', command = self.clicked)
      b2.place(x=430,y=560)
      img2 = Image.open('rmute.png')
      b3 = ImageTk.PhotoImage(img2.resize((49,25)))
      lab3 = Label(root, image = b3)
      lab3.place(x=780,y=500)
      img3 = PhotoImage(file='muteb.png')
      b4= Button(root, image=img3, bg='black', command = root.destroy)
      b4.place(x=730,y=560)
      if(0<=t1 and t1<11):
          lee_voice("good Morning! How can I help you")
      elif(11<=t1 and t1<18):
          lee_voice("good Afternoon  How can I help you")
      elif(18<=t1 and t1<24):
          lee_voice("good evening  How can I help you")
      root.mainloop()    


  def clicked(self):
    print("working...")
    voice_data1=''
    voice_data2=''
    voice_data1 = record_audio()
    voice_data2 = voice_data1.lower()
    

    if 'who are you' in voice_data2:
        lee_voice('I am your Virtual Assistant I can be very helpful in getting your work done easier ,with my assistance')

    if 'open youtube' in voice_data2:
        print('entered')
        search = record_audio('What do you want to watch?')
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)
        
    if 'i want to search' in voice_data2:
        search = record_audio('What do you want to search for ?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        summ = wk.summary(search)
        summary1 = summ.split('.')
        summary2 = ' '.join(str(e) for e in summary1[:3])
        try:
            lee_voice('Here is the short note on the content you asked for' + summary2)
        except:
            lee_voice('Sorry your search could not be found')
        

    if 'set me a destination' in voice_data2:
        location = record_audio('where do you want to go?')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        lee_voice('Here is location' + location)
    if 'what is the time' in voice_data2:
        t = time.asctime().split(' ')
        print(t[3])
        lee_voice(t[3])

  #  if 'what is the time' in voice_data:
    #  lee_voice("Sir the time is :" + ctime())
    
    if 'exit' in voice_data2:
      lee_voice('Thanks have a good day ')
      exit()
    if 'vehicle detection' in voice_data2:
        import vehicle

    if 'road lane' in voice_data2:
        import main1
    
    if 'location' in voice_data2:
	    res1 = requests.get('https://ipinfo.io/')
	    data = res1.json()
	    city = data['city']

	    location = data['loc'].split(',')
	    latitude = location[0]
	    longitude = location[1]
	    address=data['country']
	    print("Latitude value :", latitude)
	    lee_voice("Latitude value is {}".format(latitude))
	    print("Longitude value: ", longitude)
	    lee_voice("Longitude value is {}".format(longitude))
	    print("Captial City : ", city)
	    lee_voice("Captial City Name is {}".format(city))
	    print("Country :",address)
	    lee_voice("Country name is {}".format(address))    
            #lee_voice('hi') '''   

if __name__ == '__main__':
        widget = Widget()

time.sleep(1)
while 1:
  voice_data = record_audio()
  respond(voice_data)


speaker.runAndWait()
