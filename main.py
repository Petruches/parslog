#!/usr/bin/env python3

TEXT_SESSION: str = "ERROR"
file = open("./log.log", 'r')


def send_telegram(text: str):
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
        raise Exception("post_text error")

send_telegram("asdasdasdasd")

def start():
    print("start")
    while True:
        chunk = file.readline()
        if not chunk:
            continue
        elif TEXT_SESSION in chunk:
            print(chunk)

# start()
