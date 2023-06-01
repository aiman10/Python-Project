import subprocess
def run_cmd(command):
    subprocess.check_call(command.split(' '))
