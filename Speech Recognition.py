import speech_recognition as sr

recognizer = sr.Recognizer()

with  sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source, timeout=5)

try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print(f"Couldn't connect with google. Try again later... {sr.RequestError}")


