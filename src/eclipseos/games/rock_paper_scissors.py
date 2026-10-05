from eclipseos.commands.help import AddToCommands
import random

class RockPaperScissors:
    def __init__(self, command, description):
        self.bot = random.choice(['rock', 'paper', 'scissors'])

        self.command = command
        self.description = description

        add_command = AddToCommands(self.command, self.description)
        add_command.execute()

    def execute(self):
        human = input('>> ')
        if human not in ['rock', 'paper', 'scissors']:
            print(f'Error occurred\nanswer not in options\nyour answer = {human}')
        elif human == "rock" and self.bot == "paper":
            print(f'You lost\nbot: {self.bot}\nhuman: {human}')
        elif human == 'scissors' and self.bot == "rock":
            print(f'You lost\nbot: {self.bot}\nhuman: {human}')
        elif human == 'paper' and self.bot == "scissors":
            print(f'You lost\nbot: {self.bot}\nhuman: {human}')
        elif human == self.bot:
            print(f'Draw\nbot: {self.bot}\nhuman: {human}')
        else:
            print(f'You won\nbot: {self.bot}\nhuman: {human}')

rock_paper_scissors = RockPaperScissors('rock_paper_scissors / rps', 'start a rock paper scissors game')