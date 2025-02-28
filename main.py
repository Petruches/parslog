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
        print("sykaaa: ", e)


async def start(url: str, channel_id: str):
    try:
        import os
        os.path.isfile("./log.log")
        # await asyncio.create_task(health_check(url))
        while True:
            chunk = FILE.read(50000)
            lst: list[str] = chunk.split("\n")
            if not chunk:
                continue
            for i in range(len(lst)):
                if TEXT_SESSION in lst[i]:
                    await asyncio.create_task(health_check(url))
                    await asyncio.create_task(send_telegram(str(lst[i]), url, channel_id))
            continue
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(start(argv[1], argv[2]))
