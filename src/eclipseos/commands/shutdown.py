import os

class Power:
    def __init__(self, action):
        self.action = action

    def execute(self, answer):
        if 'sudo' not in answer:
            print('permission denied')
            return
        os.system(self.action)


shutdown = Power('sudo shutdown now')
reboot = Power('sudo reboot')