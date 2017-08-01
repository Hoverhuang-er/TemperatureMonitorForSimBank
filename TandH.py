import sys
import requests
import threading
import uploadYeelink
import dataprocess
import ReqT
import time
import wx
import json
from Quene import Quene
from pytimer import Timer
@Timer(average=False)


temperature_c = 'https://us.wio.seeed.io/v1/node/GroveTempHumD0/temperature?access_token=760369546a5f1ff89282dfed8eac9d7d'
humanity = 'https://us.wio.seeed.io/v1/node/GroveTempHumD0/humidity?access_token=760369546a5f1ff89282dfed8eac9d7d'
dust = 'https://us.wio.seeed.io/v1/node/GroveLuminanceA0/luminance?access_token=760369546a5f1ff89282dfed8eac9d7d'

r = requests.get()
#requests.post("http://maker.ifttt.com/trigger/HOGEHOGE/with/key/FUGAFUGA, json={"value1": "Hello, IFTTT!"})
print ("r.content"

    for requests.get('https://us.wio.seeed.io/v1/node/GroveTempHumD0/temperature?access_token=760369546a5f1ff89282dfed8eac9d7d')
    in range (10)
    for requests.get(humanity_get_api) in range (10)
    for get_urls(dust_get_api) in range (10))

def get_url(temperature_c_get_api):
    r = requests.get(temperature_c_get_api)
    print("r.temperature_c_get_api")
    if status_code != 400
        requests.get(temperature_c_get_api)


def get_url(humanity_get_api):
    r = requests.get(humanity_get_api)
    print("r.humanity_get_api")
    if status_code != 400
        requests.get(humanity_get_api)


def get_url(dust_get_api):
    r = requests.get(dust_get_api)
    print("r.dust_get_api")
    if status_code != 400
        requests.get(dust_get_api)


def post_url(sleep_time_post_api):
    r = requests.post(sleep_time_post_api)
    print("r.status_code")
    if status_code = 200
    print
    "Okay"
    elif status_code: 400
    print
    ("error")


def main(argv1):
    temperature_c_get_api = argv1
    if status = 200:
        temperature_c_get_api = [temperature_c_get_api]
    elif status == 400:
        urls = [sleep_time_post_api]


def main(argv2):
    humanity_get_api = argv2
    if status = 200
    humanity_get_api = [humanity_get_api]
    elif status == 400:
    url = [sleep_time_post_api]


def main(argv3):
    dust_get_api = argv3
    if status = 200
    dust_get_api = [dust_get_api]
    elif status == 400:
    url = [dust_get_api]
def main(timer)

for temperature_c_get_api in temperature_c_get_api:
    threading.Thread(target=temperature_c_get_api, argv1=(temperature_c_get_api))，start()
for humanity_get_api in humanity_get_api:
    threading.Thread(target=humanity_get_api, argv2=(humanity_get_api)), start()
for dust_get_api in dust_get_api:
    threading.Thread(target=dust_get_api, argv3=(dust_get_api)), start()

def matmul(a,b,times=180):



if __name__ == '__main__':
    if len(sys.argv) !=4
        print("system using")
        exit(1)
    main(sys,argv[1])
    main(sys,argv[2])
    main(sys.argv[3])

with open ('celsius_degree ()','w') as outfile:
    json.dump(temperature_c,outfile)
with open ('dust ()','w') as outfile:
    json.dump(dust,outfile)
with open('humidity ()','w')as outfile:
    json.dump(humanity,outfile)

class _timerThread(threading.Thread):

