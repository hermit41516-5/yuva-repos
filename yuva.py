import os
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from authenticate import authenticate

engine = pyttsx3.init()

def speak(text):
    print("YUVA:", text)
    engine.say(text)
    engine.runAndWait()

def record_command(filename="command.wav"):
    samplerate = 16000
    duration = 4

    show_commands()
    print("🎤 Listening... Speak now")

    audio = sd.rec(int(duration * samplerate),
                   samplerate=samplerate,
                   channels=1,
                   dtype='int16')

    sd.wait()

    wav.write(filename, samplerate, audio)

def listen_command():
    record_command()

    r = sr.Recognizer()

    with sr.AudioFile("command.wav") as source:
        audio = r.record(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Speech service unavailable.")
        return ""

def execute_command(command):
    if "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("shutdown /s /t 1")

    elif "search" in command:
        import webbrowser
        query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak("Searching on Google")

    elif "help" in command:
        speak("You can say open notepad, shutdown, or search something.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        print(" Exiting YUVA...")
        exit()

    else:
        speak("Command not recognized.")

def show_commands():
    print("\n Available Commands:")
    print(" - open notepad")
    print(" - search <your query>")
    print(" - shutdown")
    print(" - help")
    print(" - exit")
    print("-" * 30)
def main():
    speak("Starting YUVA")

    if authenticate():
        speak("Welcome. Here are commands you can use.")
        show_commands()
        while True:
            command = listen_command()
            if command:
                execute_command(command)
    else:
        speak("Authentication failed")

if __name__ == "__main__":
    main()
