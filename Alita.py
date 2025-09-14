import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2

assistant_name = "Alita"

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change to voices[1].id if you want another voice
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

# Speak function
def speak(audio):
    print(f"[speaking]: {audio}")
    engine.say(audio)
    engine.runAndWait()

# Listen for voice commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Network error. Please check your connection.")
        except Exception:
            speak("Say that again please....")
    return ""

# Greeting
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Hi, good morning Harshita! I am {assistant_name}, your assistant.")
    elif 12 <= hour < 16:
        speak(f"Good afternoon Harshita! I am {assistant_name}, your assistant.")
    else:
        speak(f"Good evening Harshita! I am {assistant_name}, your assistant.")
    speak("How can I help you?")

# Main program
if __name__ == "__main__":
    speak("Testing voice system")   # check if voice works
    wish()
    while True:
        query = takeCommand()
        if not query:
            continue

        elif "your name" in query or "what is your name" in query:
            speak(f"My name is {assistant_name}")

        elif "open desktop" in query:
            desktop = "C:\\Program Files\\WindowsApps"
            os.startfile(desktop)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow("Webcam", img)
                k = cv2  .waitKey(1)
                if k == 27:  # ESC key to exit
                    break
            cam.release()
            cv2.destroyAllWindows()
        elif "open whatsapp" in query:
           speak("Opening WhatsApp")
           try:
            os.startfile("C:\\Users\\YourUserName\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
           except Exception:
            speak("I could not find WhatsApp. Please check the path.")



        elif any(word in query for word in ["exit", "quit", "stop"]):
            speak("Goodbye Harshita! Have a nice day!")
            break
