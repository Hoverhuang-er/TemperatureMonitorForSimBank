import requests
import datetime
os.environ["NODE_PATH"] = os.get

temperature = requests.get('https://52.221.189.109/v1/node/GroveTempHumD0/temperature?access_token=760369546a5f1ff89282dfed8eac9d7d')
print(temperature.content)
humidty = requests.get('https://52.221.189.109/v1/node/GroveTempHumD0/humidity?access_token=760369546a5f1ff89282dfed8eac9d7d')
print(humidty.content)
dust = requests.get('https://52.221.189.109/v1/node/GroveLuminanceA0/luminance?access_token=760369546a5f1ff89282dfed8eac9d7d')
print(dust.content)
temperature = requests.get('https://52.221.189.109/v1/node/GroveTempHumD0/temperature?access_token=760369546a5f1ff89282dfed8eac9d7d')
print('temperature.content')
humidty = requests.get('https://52.221.189.109/v1/node/GroveTempHumD0/humidity?access_token=760369546a5f1ff89282dfed8eac9d7d')
print('humidty.content')
dust = requests.get('https://52.221.189.109/v1/node/GroveLuminanceA0/luminance?access_token=760369546a5f1ff89282dfed8eac9d7d')
print('dust.content')

class Datatime:
    def.__import__(datetime)
    datetime.time
    print(datetime,%"n",dust)
    print(datetime,%"n",temperature)
    print(datetime,%"n",humidty)

