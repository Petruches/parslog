import subprocess


def get_uptime():
    return subprocess.check_output(['uptime'], shell=True)

print(str(get_uptime()))