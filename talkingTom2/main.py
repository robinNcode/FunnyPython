import pyttsx3

tom = pyttsx3.init()

while True:
    speech = input("Write Something: ")
    tom.say(speech)
    tom.runAndWait()
