import speech_recognition as sr
import pyttsx3
from wit import Wit
import logging
from pprint import pprint

client = Wit("CTTWNKS7IKLBJ2XWHNNZLCZJNSFL2BBJ")
rec = sr.Recognizer()

reproduction = pyttsx3.init()

def sai_som(resp):
    reproduction.say(resp)
    reproduction.runAndWait()

def response(self, entities, intents, text, traits):
    if (intents['name'] == 'action') and (intents['confidence'] > 0.6):
        if not entities:
            sai_som("não encontrei nada")
        else:
            if entities['value'] == 'on':
                sai_som('ligado')
            else:
                sai_som('desligado ligado')
    
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

                pprint(resp)

                resp_value = resp['traits']['wit$on_off'][0]['value']


                if resp_value == 'on':
                    sai_som("Acionando")
                elif resp_value == 'off':
                    sai_som("Desligando")
                else:
                    sai_som("Repita")

            except sr.UnknownValueError:
                print("Não Entendi")
            
            except KeyError:
                print("Erro de chave")
                sai_som("Erro de chave")


#client.interactive()

#resp = client.message('Ligue a luz')

#pprint(resp['traits']['wit$on_off'][0]['value'])
#print(resp['traits']['wit$on_off'][0]['value'])