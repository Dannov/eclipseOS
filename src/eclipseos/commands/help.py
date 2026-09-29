class AddToCommands:
    def __init__(self, command, description):
        self.command = command
        self.description = description

    def execute(self):
        with open('commands.txt', 'a') as file:
            file.write(str(self.command + ': ' + self.description + '\n'))

class Help:
    def __init__(self, command, description):
        self.help_command = command
        self.help_description = description

    help_add = AddToCommands(command, self.help_description)

    def execute(self):
        with open('commands.txt', 'r') as file:
            print(file.read())

help_command = Help('help', 'runs this command')
help_command.execute()

#TODO: check the super() thingy, looks like this could solve this problem, when you do that do the AddToCommands
#TODO: to the every other command so when you do help_commands.execute() it will show all of the commands