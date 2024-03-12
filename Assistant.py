import pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser
import random
import os
import wikipedia

# voice input ke lie
r = sr.Recognizer()

engine = pyttsx3.init()
voiceid = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voiceid)
engine.setProperty('volume', 1)
engine.setProperty('rate', 115)

def listen():
    while(1):
        try:
            mic = sr.Microphone(device_index=3)

            with mic as source2:

                audio2 = r.listen(source2)
                r.energy_threshold = 300
                r.pause_threshold = 1

                useraudio = r.recognize_google(audio2)
                useraudio = useraudio.lower()
                return useraudio

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            speak("Please Try Again ")


def speak(text):  # text to be spoken (text will get here via recognizer)
    """
    This function makes system to speakup
    """
    engine.say(text)
    engine.runAndWait()


def wishing():
    """
    this function wishes according to time
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good morning,{name}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon,{name}.")
    else:
        speak(f"Good evening,{name}.")


# main function calls

if __name__ == "__main__":
    speak("Who are you ?")
    print("Who are You?")
    name = listen()

    wishing()

    while True:
        # print("in while true")
        # command = listen_user().lower()

        # tasks start here
        time.sleep(0.3)
        speak("how may I help you ?")
        print("How May I help You ?")
        command = listen()

        if 'open youtube' in command:
            webbrowser.open("www.youtube.com")
            speak("opening YOUTUBE....")

        elif 'open google' in command:
            webbrowser.open('www.google.com')
            speak("opening GOOGLE....")

        elif 'tell date' in command:
            tarik = datetime.datetime.now()
            tarik1 = tarik.strftime("%A, %d, %B")
            speak(f"today is {tarik1}")

        elif 'open github' in command:
            webbrowser.open('www.github.com')
            speak("opening GITHUB....")

        elif 'how are you' in command:
            feelings = ['happy', 'sad', 'angry', 'excited']
            feel = random.choice(feelings)
            # print(feel)
            speak(f"I am feeling {feel}")
            speak(f"what about you {name} ?")
            u_feel = input()
            speak("oh !!")

            # print(type(feelings))

        elif 'tell time' in command:
            samay = datetime.datetime.now()
            samay1 = samay.strftime("%H, %M, %S")
            speak(f"current time is {samay1}")

        elif 'bye' in command:
            speak("bye, have a good day")
            exit()

        elif 'open discord' in command:
            try:

                dc = "C:\\Users\\anshu\\Desktop\\Discord.lnk"
                os.startfile(dc)
                speak("Opening Discord")
            except Exception as e:
                # print(e)
                speak("Sorry , an error occured")

        elif 'open browser' in command:
            try:

                browser = "C:\\Users\\Public\\Desktop\\Firefox Developer Edition.lnk"
                os.startfile(browser)
                speak("opening Browser...")
            except Exception as e:
                speak("sorry, an error occured")

        elif 'coin flip' in command:

            hvt = ['H', 'T']
            outcome = random.choice(hvt)
            # print(outcome)

            speak("choose Either Heads or Tails")
            print("'H' for Heads and 'T' for Tails")

            user = listen()

            if outcome == user:
                speak(f"{name} wins ")
                print(f"{name} Wins !!")

            else:
                speak("Computer Wins !!")
                print("Computer Wins !!")

        elif 'who are you' in command:
            speak(f"I'm your Assistant {name}")

        elif 'wikipedia' in command:

            speak("searching wikipedia...")
            result = wikipedia.summary(command, sentences=2)

            print("According to wikipedia", result)
            speak("According to wikipedia")
            speak(result)

        else:
            speak("Sorry , I don't know that..")
