from pprint import pprint
from modules.sound_output import speak

def analysis(content):
    """
    This function identify the context and give an answer
    """
    if not content['intents']:
        speak('Não entendi. Por favor repita a pergunta')
    elif content['intents'][0]['name'] == 'greeting':
        speak('Olá, como posso ajudar?')
    elif content['intents'][0]['name'] == 'action':
        if not content['traits']:
            speak('Não entendi. Pergunte novamente!')
        elif content['traits']['wit$on_off']:
            if not content['entities']:
                speak('Não entendi!')
            else:
                if not content['entities']['wit$location:location']:
                    speak('Em qual lugar?')
                else:
                    if content['traits']['wit$on_off'][0]['value'] == 'on':
                        speak(content['entities']['wit$location:location'][0]['value'] + ': ligando ' + content['entities']['device:device'][0]['value'])
                    else:
                        speak(content['entities']['wit$location:location'][0]['value'] + ': desligando ' + content['entities']['device:device'][0]['value'])