from eclipseos.commands.help import AddToCommands
import os

class Power:
    def __init__(self, action, command, description):
        self.action = action

        self.command = command
        self.description = description

        add_command = AddToCommands(self.command, self.description)
        add_command.execute()

    def execute(self, answer):
        if 'sudo' not in answer:
            print('permission denied')
            return
        os.system(self.action)


shutdown = Power('sudo shutdown now', 'shutdown' , 'turns off the pc')
reboot = Power('sudo reboot', 'reboot' , 'reboots off the pc')