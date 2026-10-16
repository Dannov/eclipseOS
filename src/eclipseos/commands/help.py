commands = []

class AddToCommands:
    def __init__(self, command, description):
        self.command = command
        self.description = description

    def execute(self):
        commands.append(str(self.command + ': ' + self.description))

class Help:
    def __init__(self, command, description):
        self.command = command
        self.description = description
        add_command = AddToCommands(self.command, self.description)
        add_command.execute()

    def execute(self):
        print('\n'.join(commands))

help_command = Help('help', 'runs this command')
