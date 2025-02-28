#!/usr/bin/env python
import requests
from sys import argv
import asyncio

TEXT_SESSION: str = "ERROR"
FILE = open("./log.log", 'r')


@staticmethod
async def health_check(url: str):
    r = requests.get(f"{url}/getMe")
    if r.status_code != 200:
        raise "status code does not 200"


@staticmethod
async def send_telegram(text: str, url_tg: str, channel_id_tg: str):
    try:
        url = url_tg
        channel_id = channel_id_tg
        method = url + "/sendMessage"
        r = requests.post(method, data={
            "chat_id": channel_id,
            "text": text
        })
    except Exception as e:
        print("Error: ", e)


async def check_error(lst: list[str], url: str, channel_id: str):
    for i in range(len(lst)):
        if TEXT_SESSION in lst[i]:
            await asyncio.create_task(send_telegram(str(lst[i]), url, channel_id))
        continue


async def start(url: str, channel_id: str):
    try:
        import os
        #os.path.isfile("./log.log")
        while True:
            chunk = FILE.read(50000)
            lst: list[str] = chunk.split("\n")
            if not chunk:
                continue
            await asyncio.create_task(check_error(lst, url, channel_id))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(start(argv[1], argv[2]))
