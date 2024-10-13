#!/bin/bash

PTH=/home/petr/Desktop/python/project1/parsbot/file/uptime.txt

echo $PTH
uptime > $PTH 2>/dev/null
