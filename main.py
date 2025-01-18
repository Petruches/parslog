#!/usr/bin/env python
import requests
from sys import argv

TEXT_SESSION: str = "ERROR"
FILE = open("./log.log", 'r')


def health_check(url: str):
    r = requests.get(f"{url}/getMe")
    if r.status_code != 200:
        raise "status code does not 200"

def send_telegram(text: str, url_tg: str, channel_id_tg: str) -> None:
    try:
        url = url_tg
        channel_id = channel_id_tg
        method = url + "/sendMessage"
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })
        health_check(url)
    except Exception as e:
        print("sykaaa: ", e)


def start(url: str, channel_id: str) -> None:
    try:
        import os
        os.path.isfile("./log.log")
        while True:
            chunk = FILE.read(50000)
            lst: list[str] = chunk.split("\n")
            if not chunk:
                continue
            for i in range(len(lst)):
                if TEXT_SESSION in lst[i]:
                    send_telegram(str(lst[i]), url, channel_id)
                    print(lst[i])
            continue
    except Exception as e:
        print(e)


if __name__ == "__main__":
    start(argv[1], argv[2])
