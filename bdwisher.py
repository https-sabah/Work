import pandas as pd
import datetime
import pyttsx3
from plyer import notification, vibrator

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)  # Volume should be a float between 0.0 and 1.0

engine.say("Hello Sabah, welcome to your program")
engine.runAndWait()

# Function for sending a notification
def notify(title, msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon=r"C:\Users\Sabah Nizami\Desktop\bithday wisher\Birthday-cake.icon.ico",  # file path for icom
        timeout=8
    )

# Load the birthday data
dates = pd.read_excel(r"C:\Users\Sabah Nizami\Desktop\Bithday wisher\Birthday dates.xlsx") # xlsx file path
today = datetime.datetime.now().strftime("%d-%m")

# Function for speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Check birthdays
for i, item in dates.iterrows():
    bd_date = item["D.O.B"]  # column name is DOB in Excel
    if today == bd_date.strftime("%d-%m"):  # date matching
        name = item["NAME"]  # column is NAME in Excel
        message = f"Today is {name}'s birthday!"
        notify("Birthday Reminder", message)
        speak(f"Sabah, today is {name}'s birthday.")
