import speech_recognition as sr
import pyttsx3 as pt
import webbrowser
import subprocess
import musicLibrary
import desktop


websites = {
    "youtube": "https://www.youtube.com/",
    "facebook": "https://www.facebook.com/",
    "gmail": "https://www.gmail.com/",
    "instagram": "https://www.instagram.com/"
}


recognizer = sr.Recognizer()
engine = pt.init()


while True:

    try:
        # Wake word sunna
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source,phrase_time_limit=3)

        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Jarvis detect hua
        if "friday" in text.lower():

            engine.say("Yes Sir")
            engine.runAndWait()

            # COMMAND MODE
            while True:

                with sr.Microphone() as source:
                    print("Listening for command...")
                    command_audio = recognizer.listen(source, phrase_time_limit=4)

                command = recognizer.recognize_google(command_audio)
                print("Command:", command)

                command = command.lower()

                # Sleep command
                if "sleep" in command:
                    engine.say("Okay Sir")
                    engine.runAndWait()
                    break

                # Website commands
                for site in websites:

                    if site in command:
                        engine.say(f"Opening {site} sir.")
                        engine.runAndWait()

                        webbrowser.open(websites[site])
                        break

                # Music commands
                for song in musicLibrary.musics:

                    if song in command:
                        engine.say(f"Playing {song} sir.")
                        engine.runAndWait()

                        webbrowser.open(musicLibrary.musics[song])
                        break

                # Application commands
                for app in desktop.apps:

                    if app in command:
                        engine.say(f"Opening {app} sir.")
                        engine.runAndWait()

                        subprocess.Popen(
                            ["open", "-a", desktop.apps[app]]
                        )
                        break


    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

    except sr.WaitTimeoutError:
        print("No speech detected.")

    except sr.RequestError:
        print("Google Speech Recognition service is unavailable.")
