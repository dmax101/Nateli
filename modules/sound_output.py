import pyttsx3

def speak(resp):
    """
    This function speak to user an answer
    """
    reproduction = pyttsx3.init()
    reproduction.say(resp)
    reproduction.runAndWait()