# Nateli - Home Assistant
# Author Danilo Ribeiro
# Scientific Initiation Scholarships Project
# Jul - 2020

import speech_recognition as sr
from pprint import pprint
import json


from modules.wit_connector import wit_connection
from modules.wit_connector import wit_attributes
from modules.sound_output import speak
from modules.analysis import analysis

auth_token = "PG4WVUCICSUSXDDKHF76RXPPOOMMOR2V"

client = wit_connection(auth_token)

rec = sr.Recognizer()



speak("Bem vindo!")

while True:
    print("inicializando...")
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        while True:
            try:
                print("ouvindo...")
                audio = rec.listen(s)
                entrada = rec.recognize_google(audio, language="pt")
                print("Você disse: {}".format(entrada))

                resp = client.message(entrada)

                pprint(resp)

                analysis(resp)

            except sr.UnknownValueError:
                print("Não Entendi")
            
            except KeyError:
                speak("Não entendi, poderia repetir por favor?")
                print("Erro de chave")
