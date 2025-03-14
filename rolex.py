import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import time
import subprocess
import requests
import json
import smtplib
import random
import wolframalpha
import re
import wikipedia
from translate import Translator
import dotenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I could not understand your command.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service unavailable.")
            return ""
        except sr.WaitTimeoutError:
            speak("No speech detected. Try again.")
            return ""

def open_application(app_name):
    app_paths = {
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "notepad": "notepad.exe",
        "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
        "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
        "spotify": "C:\\Users\\Username\\AppData\\Roaming\\Spotify\\Spotify.exe"
    }
    
    for key in app_paths:
        if key in app_name:
            subprocess.Popen(app_paths[key], shell=True)
            return
    speak("Application not recognized.")

def set_alarm(time_str):
    try:
        alarm_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        speak(f"Alarm set for {time_str}")
        while True:
            if datetime.datetime.now().strftime("%H:%M") == time_str:
                speak("Time to wake up!")
                break
            time.sleep(60)
    except ValueError:
        speak("Invalid time format. Please use HH:MM format.")

def schedule_meeting(meeting_time, meeting_link):
    if meeting_time and meeting_link:
        speak(f"Scheduling meeting at {meeting_time}.")
        webbrowser.open(meeting_link)
    else:
        speak("Invalid meeting details.")

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        speak("Weather API key not found.")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        weather_data = response.json()
        if weather_data.get("main"):
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            speak(f"The current temperature in {city} is {temp} degrees Celsius with {description}.")
        else:
            speak("Sorry, I couldn't fetch the weather details.")
    except requests.RequestException:
        speak("Unable to fetch weather details due to network issues.")

def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        speak("News API key not found.")
        return
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get("articles", [])[:5]
        if articles:
            for article in articles:
                speak(article["title"])
        else:
            speak("No news articles found.")
    except requests.RequestException:
        speak("Unable to fetch news at the moment.")

def convert_currency(command):
    match = re.search(r"convert (\d+(?:\.\d+)?) (\w{3}) to (\w{3})", command)
    if match:
        amount, from_currency, to_currency = float(match.group(1)), match.group(2).upper(), match.group(3).upper()
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        try:
            response = requests.get(url)
            data = response.json()
            rate = data["rates"].get(to_currency)
            if rate:
                converted_amount = amount * rate
                speak(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
            else:
                speak("Currency conversion failed.")
        except requests.RequestException:
            speak("Unable to fetch exchange rates at the moment.")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    joke = random.choice(jokes)
    speak(joke)

def tell_quote():
    quotes = [
        "The best way to predict your future is to create it. - Abraham Lincoln",
        "You miss 100% of the shots you don’t take. - Wayne Gretzky",
        "Whether you think you can or you think you can’t, you’re right. - Henry Ford"
    ]
    quote = random.choice(quotes)
    speak(quote)

def send_email(to_address, subject, body):
    from_address = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    if not from_address or not password:
        speak("Email credentials not found.")
        return
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_address, password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(from_address, to_address, message)
        speak("Email sent successfully.")
    except smtplib.SMTPException:
        speak("Failed to send email.")

def wolfram_query(query):
    app_id = os.getenv("WOLFRAM_APP_ID")
    if not app_id:
        speak("WolframAlpha App ID not found.")
        return
    
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(query)
        answer = next(res.results).text
        speak(answer)
    except Exception as e:
        speak("I couldn't fetch an answer from WolframAlpha.")

def wikipedia_search(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No result found on Wikipedia.")

def translate_text(text, to_lang):
    translator = Translator(to_lang=to_lang)
    translation = translator.translate(text)
    speak(translation)

def process_command(command):
    if "open" in command:
        open_application(command.replace("open", "").strip())
    elif "set alarm for" in command:
        set_alarm(command.replace("set alarm for", "").strip())
    elif "schedule meeting" in command:
        details = command.replace("schedule meeting", "").strip().split(" at ")
        if len(details) == 2:
            schedule_meeting(details[0], details[1])
    elif "weather in" in command:
        get_weather(command.replace("weather in", "").strip())
    elif "news update" in command:
        get_news()
    elif "convert" in command:
        convert_currency(command)
    elif "tell me a joke" in command:
        tell_joke()
    elif "quote" in command:
        tell_quote()
    elif "send email" in command:
        details = command.replace("send email to", "").strip().split(" subject ")
        if len(details) == 2:
            recipient, subject_body = details[0].strip(), details[1].strip().split(" body ")
            if len(subject_body) == 2:
                subject, body = subject_body[0].strip(), subject_body[1].strip()
                send_email(recipient, subject, body)
    elif "wolfram" in command:
        wolfram_query(command.replace("wolfram", "").strip())
    elif "search wikipedia for" in command:
        wikipedia_search(command.replace("search wikipedia for", "").strip())
    elif "translate" in command:
        details = command.replace("translate", "").strip().split(" to ")
        if len(details) == 2:
            text, to_lang = details[0].strip(), details[1].strip()
            translate_text(text, to_lang)
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that. Can you repeat?")

if __name__ == "__main__":
    speak("Hello! I am Rolex, your AI assistant. How can I help you?")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)