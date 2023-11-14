import pyttsx3

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greeting(self):
        self.speak("Hello, I am your personal assistant. How can I help you?")
