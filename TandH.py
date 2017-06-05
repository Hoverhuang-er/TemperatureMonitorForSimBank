import sys
import requests
import timer
import threading

temperature_c_get_api =
humanity_get_api =
dust_get_api =
sleep_time_post_api =

for get_url(temperature_c_get_api) in range (10)
for get_url(humanity_get_api) in range (10)
for get_url(dust_get_api) in range (10)

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
    "error"


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


for temperature_c_get_api in temperature_c_get_api:
    threading.Thread(target=temperature_c_get_api, argv1=(temperature_c_get_api))，start()
for humanity_get_api in humanity_get_api:
    threading.Thread(target=humanity_get_api, argv2=(humanity_get_api)), start()
for dust_get_api in dust_get_api:
    threading.Thread(target=dust_get_api, argv3=(dust_get_api)), start()




if __name__ == '__main__':
    if len(sys.argv) !=4
        print("system using")
        exit(1)
    main(sys,argv[1])
    main(sys,argv[2])
    main(sys.argv[3])

