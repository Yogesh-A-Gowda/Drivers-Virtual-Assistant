import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import os
import random
from gtts import gTTS
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import subprocess
import json
import requests
import wikipedia as wk
import re
import pyaudio # Import PyAudio
import wave # Import the wave module for reading WAV files

# --- Global variables and initial setup ---
t = time.asctime().split(" ")
t2 = t[3].split(":")
tt1 = (t2[0])
print(tt1)
t1 = int(tt1)
print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init() # Initialized, but not used for speech output with gTTS/PyAudio

# --- Functions ---

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print('Listening...')
        audio = r.listen(source, phrase_time_limit=5)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :' + voice_data)
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio (UnknownValueError).')
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e} (RequestError).")
        except Exception as e:
            print(f'An unexpected error occurred during recognition: {e}')
        return voice_data

def lee_voice(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r_val = random.randint(1, 1000000)
    audio_file_mp3 = 'audio-' + str(r_val) + '.mp3'
    tts.save(audio_file_mp3)

    wav_file = 'audio-' + str(r_val) + '.wav'

    # Hardcoded FFmpeg path
    ffmpeg_executable_path = r"D:\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"

    ffmpeg_command = [ffmpeg_executable_path, '-i', audio_file_mp3, '-y', wav_file]
    print(f"Executing FFmpeg command: {' '.join(ffmpeg_command)}")

    try:
        result = subprocess.run(ffmpeg_command, check=True, capture_output=True)
        print("FFmpeg conversion successful.")

        if not os.path.exists(wav_file) or os.path.getsize(wav_file) == 0:
            print(f"Generated WAV file '{wav_file}' is missing or empty. Cannot play.")
            return

        try:
            wf = wave.open(wav_file, 'rb')

            p = pyaudio.PyAudio()

            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            chunk_size = 1024
            data = wf.readframes(chunk_size)
            while data:
                stream.write(data)
                data = wf.readframes(chunk_size)

            stream.stop_stream()
            stream.close()
            wf.close()
            p.terminate()
            print("Audio played successfully via PyAudio.")

        except Exception as py_e:
            print(f"PyAudio playback failed: {py_e}")

    except FileNotFoundError:
        print("FFmpeg executable not found. Check 'ffmpeg_executable_path'.")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg conversion failed (exit code {e.returncode}):")
        print(f"  STDOUT: {e.stdout.decode()}")
        print(f"  STDERR: {e.stderr.decode()}")
    except Exception as e:
        print(f"An unexpected error occurred in lee_voice (FFmpeg/overall): {e}")
    finally:
        if os.path.exists(audio_file_mp3):
            os.remove(audio_file_mp3)
        if os.path.exists(wav_file):
            os.remove(wav_file)

def respond(voice_data):
    voice_data2 = voice_data.lower()

    if 'who are you' in voice_data2:
        lee_voice('I am your Virtual Assistant. I can be very helpful in getting your work done easier, with my assistance.')

    elif 'open youtube' in voice_data2:
        print('entered')
        search = record_audio('What do you want to watch?')
        if search:
            url = f'https://www.youtube.com/results?search_query={search.replace(" ", "+")}'
            webbrowser.get().open(url)
            lee_voice(f'Opening YouTube and searching for {search}')
        else:
            lee_voice('Sorry, I did not catch what you want to watch on YouTube.')

    elif 'i want to search' in voice_data2:
        search = record_audio('What do you want to search for?')
        if search:
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            try:
                summ = wk.summary(search, sentences=3)
                lee_voice('Here is a short note on the content you asked for: ' + summ)
            except wk.exceptions.PageError:
                lee_voice('Sorry, your search could not be found on Wikipedia.')
            except wk.exceptions.DisambiguationError as e:
                lee_voice(f"Your search term is ambiguous. Please be more specific. Options include: {', '.join(e.options[:5])}")
            except Exception as e:
                lee_voice(f'An error occurred during Wikipedia search: {e}')
        else:
            lee_voice('Sorry, I did not catch what you want to search for.')

    elif 'set me a destination' in voice_data2:
        location = record_audio('Where do you want to go?')
        if location:
            url = f'https://www.google.com/maps/search/{location.replace(" ", "+")}'
            webbrowser.get().open(url)
            lee_voice(f'Here is the location for {location}')
        else:
            lee_voice('Sorry, I did not catch the destination.')

    elif 'what is the time' in voice_data2:
        current_time = time.strftime("%I:%M %p")
        print(current_time)
        lee_voice(f"The current time is {current_time}")

    elif 'exit' in voice_data2:
        lee_voice('Thanks, have a good day!')
        exit()

    elif 'vehicle detection' in voice_data2:
        lee_voice("Opening vehicle detection module.")
        try:
            import vehicle
        except ImportError:
            lee_voice("Sorry, the vehicle detection module could not be found.")
        except Exception as e:
            lee_voice(f"An error occurred while running vehicle detection: {e}")

    elif 'road lane' in voice_data2:
        lee_voice("Opening road lane detection module.")
        try:
            import main1
        except ImportError:
            lee_voice("Sorry, the road lane detection module could not be found.")
        except Exception as e:
            lee_voice(f"An error occurred while running road lane detection: {e}")

    elif 'location' in voice_data2:
        try:
            res1 = requests.get('https://ipinfo.io/')
            data = res1.json()
            city = data.get('city', 'unknown city')
            location_coords = data.get('loc', '0,0').split(',')
            latitude = location_coords[0]
            longitude = location_coords[1]
            country = data.get('country', 'unknown country')

            lee_voice(f"Your current location details are: Latitude {latitude}, Longitude {longitude}, City {city}, Country {country}.")

        except requests.exceptions.RequestException as e:
            lee_voice(f"Could not retrieve location. Error: {e}")
        except json.JSONDecodeError:
            lee_voice("Could not decode location data.")
        except Exception as e:
            lee_voice(f"An unexpected error occurred while getting location: {e}")
    else:
        if voice_data:
            lee_voice("Sorry, I didn't understand that command. Can you please rephrase?")


# --- Tkinter Widget Class ---
class Widget:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1360x768')
        load = Image.open('carbgf.jpg')
        rend = ImageTk.PhotoImage(load)
        img_label = Label(self.root, image=rend)
        img_label.image = rend
        img_label.place(x=0, y=0)
        self.root.title("Drivers Virtual Assistant")
        lab1 = Label(self.root, text="Driver's Virtual Assistant", font=("agency FB", 70, 'bold'), fg='#883935', bg='#1A1112', activebackground='#1A1112')
        lab1.pack(side='top', pady=30)

        img = Image.open('gmic1.jpg')
        self.b_icon = ImageTk.PhotoImage(img.resize((25, 49)))
        lab2 = Label(self.root, image=self.b_icon)
        lab2.place(x=500, y=480)

        self.img1_button = PhotoImage(file='spkb.png')
        b2 = Button(self.root, image=self.img1_button, bg='black', command=self.clicked)
        b2.place(x=430, y=560)

        img2 = Image.open('rmute.png')
        self.b3_icon = ImageTk.PhotoImage(img2.resize((49, 25)))
        lab3 = Label(self.root, image=self.b3_icon)
        lab3.place(x=780, y=500)

        self.img3_button = PhotoImage(file='muteb.png')
        b4 = Button(self.root, image=self.img3_button, bg='black', command=self.root.destroy)
        b4.place(x=730, y=560)

        if 0 <= t1 < 11:
            lee_voice("Good Morning! How can I help you?")
        elif 11 <= t1 < 18:
            lee_voice("Good Afternoon! How can I help you?")
        elif 18 <= t1 < 24:
            lee_voice("Good Evening! How can I help you?")
        self.root.mainloop()

    def clicked(self):
        print("Button clicked. Listening for command...")
        voice_data1 = record_audio()
        if voice_data1:
            respond(voice_data1)
        else:
            lee_voice("Sorry, I didn't catch that. Please try again.")

# --- Main execution block ---
if __name__ == '__main__':
    widget = Widget()
