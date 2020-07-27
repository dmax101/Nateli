import speech_recognition as sr
import pyttsx3
from wit import Wit
import logging
from pprint import pprint

client = Wit("CTTWNKS7IKLBJ2XWHNNZLCZJNSFL2BBJ")
rec = sr.Recognizer()

reproduction = pyttsx3.init()

def sai_som(response):
    reproduction.say(response)
    reproduction.runAndWait()

while True:
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        while True:
            try:
                audio = rec.listen(s)
                audio_txt = rec.recognize_google(audio, language="pt")
                print("Você disse: {}".format(audio_txt))

                resp = client.message(audio_txt)

                resp_value = resp['traits']['wit$on_off'][0]['value']


                if resp_value == 'on':
                    sai_som("Acionando")
                elif resp_value == 'off':
                    sai_som("Desligando")
                else:
                    sai_som("Repita")

            except sr.UnknownValueError:
                print("Erro")


#client.interactive()

#resp = client.message('Ligue a luz')

#pprint(resp['traits']['wit$on_off'][0]['value'])
#print(resp['traits']['wit$on_off'][0]['value'])