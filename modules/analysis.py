from pprint import pprint
from modules.sound_output import speak
from modules.openweather import get_weather
from modules.geolocation import get_geolocation
from googletrans import Translator

def analysis(content):
    """
    This function identify the context and give an answer
    """
    if not content['intents']:
        speak('Não entendi. Por favor repita a pergunta')
    elif content['intents'][0]['name'] == 'greeting':
        speak('Olá, como posso ajudar?')
    elif content['intents'][0]['name'] == 'location_get':
        city = get_geolocation()['city']
        speak('{} é a cidade onde estamos'.format(city))
    elif (content['intents'][0]['name'] == 'weather') or (content['intents'][0]['name'] == 'temperature_get'):


        city = get_geolocation()['city']
        print(city)
        weather = get_weather(city)

        print(weather)

        temp = int(round(weather['main']['temp'], 0))
        #temp_min = int(round(weather['main']['temp_min'], 0))
        #temp_max = int(round(weather['main']['temp_max'], 0))
        translator = Translator()
        weather_description = translator.translate(weather['weather'][0]['description'], dest='pt').text


        #print('{}: A temperatura é de {} graus Celcios com máxima de {} e mínima de {}'.format(city, temp, temp_max, temp_min))
        #speak('{}: A temperatura é de {} graus Celcios com máxima de {} e mínima de {}'.format(city, temp, temp_max, temp_min))
        
        print('{}: A temperatura é de {} graus Celcios com {}'.format(city, temp, weather_description))
        speak('{}: A temperatura é de {} graus Celcios com {}'.format(city, temp, weather_description))
        
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