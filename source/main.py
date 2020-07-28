# Nateli - Home Assistant
# Author Danilo Ribeiro
# Scientific Initiation Scholarships Project
# Jul - 2020

import speech_recognition as sr
import pyttsx3
from wit import Wit
import logging
from pprint import pprint
import requests
import json

auth_token = "PG4WVUCICSUSXDDKHF76RXPPOOMMOR2V"
hed = {'Authorization': 'Bearer ' + auth_token}
url = 'https://api.wit.ai/entities?v=20200728'

client = Wit(auth_token)
entities_list = requests.get(url, headers=hed)



rec = sr.Recognizer()

reproduction = pyttsx3.init()


pprint(entities_list.json())

def sai_som(resp):
    reproduction.say(resp)
    reproduction.runAndWait()

def response(entities, intents, text, traits):
    if (intents['name'] == 'action'):
        if not entities:
            sai_som("não encontrei nada")
        else:
            if traits['value'] == 'on':
                sai_som('ligando {}'.format(entities['room:room']['value']))
            else:
                sai_som('desligado {}'.format(entities['room:room']['value']))
    
def response_checker(self, response):
    if not response:
        return False

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

                #pprint(resp)

                entities = resp['entities']
                pprint(entities)
                
                if not entities:
                    print(False)
                else:
                    print(True)

                #intents = resp['intents']
                #text = resp['text']
                #traits = resp ['traits']

                #response(entities, intents, text, traits)


                ######################################

                # resp_value = resp['traits']['wit$on_off'][0]['value']

                # if resp_value == 'on':
                #    sai_som("Acionando")
                #elif resp_value == 'off':
                #    sai_som("Desligando")
                #else:
                #    sai_som("Repita")

                ######################################



            except sr.UnknownValueError:
                print("Não Entendi")
            
            except KeyError:
                print("Erro de chave")
                sai_som("Erro de chave")


#client.interactive()

#resp = client.message('Ligue a luz')

#pprint(resp['traits']['wit$on_off'][0]['value'])
#print(resp['traits']['wit$on_off'][0]['value'])