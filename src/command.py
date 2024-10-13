import subprocess
import time
from collections import deque
import os

class Command:
    text: str = "ERROR"
    text_session: str = "New session"

    @staticmethod
    def get_uptime():
        return subprocess.check_output(['uptime'])

    @staticmethod
    def get_up():
        with open('/home/petr/Desktop/python/project1/parsbot/file/uptime.txt', 'r') as file:
            content = file.read()
        return content

    def read_file(self):
        while os.path.isfile("/var/log/auth.log"):
            with open('/var/log/auth.log', 'r') as file:
                for line in file:
                    [last_line] = deque(file, maxlen=1) or ['']
                    if self.text_session in last_line:
                        print(last_line)
                    time.sleep(10)
