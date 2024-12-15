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
        if r.status_code != 200:
            raise print(Exception)
    except Exception as e:
        print(e)


def start() -> None:
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
            continue
    except Exception as e:
        print(e)

start()
