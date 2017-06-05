import requests
import json,time


apiheaders = {'U-api':''}

yee_json_upload_api_url = ''




if __name__ == '_main_':

     while 1:
             file={'json':open('TandH.json',rb)}
             r=requests.post(yee_json_upload_api_url,json=json,headers=apiheaders)
             print('r',r)
             time.sleep(30)

