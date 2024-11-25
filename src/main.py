#!/usr/bin/python3.11
TEXT_SESSION: str = "ERROR"
file = open("/home/petr/Desktop/python/project1/parsbot/log.log", 'r')

def start():
    print("start")
    while True:
        chunk = file.readline()
        if not chunk:
            continue
        elif TEXT_SESSION in chunk:
            print(chunk)

start()
