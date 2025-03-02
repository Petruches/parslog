#!/usr/bin/env python
import requests
from sys import argv
import asyncio
from threading import Thread

TEXT_SESSION: str = "ERROR"
FILE = open("./log.log", 'r')


@staticmethod
async def health_check(url: str):
    r = requests.get(f"{url}/getMe")
    if r.status_code != 200:
        raise "status code does not 200"


@staticmethod
def send_telegram(text: str, url_tg: str, channel_id_tg: str):
    from datetime import datetime
    try:
        tm = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} - "
        url = url_tg
        channel_id = channel_id_tg
        method = url + "/sendMessage"
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": tm + text
        })
    except Exception as e:
        print("Error: ", e)


@staticmethod
def check_error(lst: list[str], url: str, channel_id: str):
    for i in range(len(lst)):
        if TEXT_SESSION in lst[i]:
            Thread(target=send_telegram, args=(str(lst[i]), url, channel_id,)).start()
        continue


async def start(url: str, channel_id: str):
    try:
        # import os
        # os.path.isfile("./log.log")
        FILE.seek(0, 2)
        while True:
            chunk = FILE.read(50000)
            lst: list[str] = chunk.split("\n")
            if not chunk:
                continue
            await asyncio.create_task(health_check(url))
            Thread(target=check_error, args=(lst, url, channel_id, )).start()
            await asyncio.sleep(1)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(start(argv[1], argv[2]))
