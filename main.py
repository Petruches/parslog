#!/usr/bin/env python

TEXT_SESSION: str = "ERROR"
FILE = open("./log.log", 'r')


def send_telegram(text: str):
    try:
        import requests
        token = "7939669010:AAEG8-KmNSVoisckbRFYM36Kq2-HkXJZWrU"
        url = "https://api.telegram.org/bot"
        channel_id = "-1002356269285"
        url += token
        method = url + "/sendMessage"
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })
        #if r.status_code != 200:
        #    raise Exception("post_text error")
    except Exception as e:
        print(e)


#send_telegram("asdasdasdasd")

def start():
    try:
        import os
        os.path.isfile("./log.log")
        while True:
            chunk = FILE.readline()
            if not chunk:
                continue
            elif TEXT_SESSION in chunk:
                send_telegram(str(chunk))
                print(chunk)
    except Exception as e:
        print(e)


start()
