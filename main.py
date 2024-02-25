# importing the pyttsx library


import pyttsx3


def speak(text, rate=150, volume=1.0):
    engine = pyttsx3.init()

    # Set properties before adding anything to speak
    engine.setProperty('rate', rate)  # Speed percent (can go over 100)
    engine.setProperty('volume', volume)  # Volume 0-1

    # Change voices (0 for male, 1 for female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Changing index changes voices

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    print("Welcome to Robo Speaker!")

    text = input("What should I say? ")
    speak(text)