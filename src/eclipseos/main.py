from .commands import fast_fetch, help_command, shutdown, reboot
from .games import rock_paper_scissors

def main():

    while True:
        answer = (input('~> ')).lower().strip()

        if answer in ('help', 'h'):
            help_command.execute()
        elif answer in ('fastfetch', 'neofetch'):
            fast_fetch.execute()
        elif answer in ('rock paper scissors', 'rps'):
            rock_paper_scissors.execute()
        elif answer in ('sudo shutdown', 'shutdown'):
            shutdown.execute(answer)
        elif answer in ('sudo reboot', 'reboot'):
            reboot.execute(answer)
        elif answer == 'exit':
            break
        else:
            print('command not found')
            continue