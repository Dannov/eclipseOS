from eclipseos.commands.fast_fetch import fast_fetch
from eclipseos.commands.shutdown import shutdown, reboot
from eclipseos.games.rock_paper_scissors import rock_paper_scissors

def main():

    with open("file.txt", "w"):
        pass

    while True:
        answer = (input('~> ')).lower().strip()

        if answer in ('fastfetch', 'neofetch'):
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