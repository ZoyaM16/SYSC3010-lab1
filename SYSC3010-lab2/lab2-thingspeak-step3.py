import urllib
import requests
import httplib
import threading
import json
import random


# Define a function that will read the server 


def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1151101/feeds.json?api_key=VI2HZL5H5PBTL725&results=2'
    KEY='VI2HZL5H5PBTL725'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(URL)

    get_data=requests.get(URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    print(feild_1)

    t=[]
    for x in feild_1:
        print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()