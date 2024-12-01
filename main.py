#!/usr/bin/env python
import time

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
        if r.status_code != 200:
            raise print(Exception)
    except Exception as e:
        print(e)


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


#start()

def start1() -> None:
    try:
        import os
        os.path.isfile("./log.log")
        while True:
            chunk = FILE.read(500000000)
            lst: list[str] = chunk.split("\n")
            if not chunk:
                continue
            for i in range(len(lst)):
                if TEXT_SESSION in lst[i]:
                    print(lst[i])
                time.sleep(1)
    except Exception as e:
        print(e)

start1()
