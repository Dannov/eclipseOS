class AddToCommands:
    def __init__(self, command, description):
        self.command = command
        self.description = description

    def execute(self):
        with open('src/eclipseos/commands.txt', 'a') as file:
            file.write(str(self.command + ': ' + self.description + '\n'))

class Help:
    def __init__(self, command, description):
        self.command = command
        self.description = description
        add_command = AddToCommands(self.command, self.description)
        add_command.execute()

    def execute(self):
        with open('src/eclipseos/commands.txt', 'r') as file:
            print(file.read())

help_command = Help('help', 'runs this command')