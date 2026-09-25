from eclipseos.commands.fast_fetch import FastFetch, fast_fetch
from eclipseos.commands.shutdown import Power, shutdown, reboot


def main():

    while True:
        answer = str(input('~> '))

        if answer == 'fastfetch' or answer == 'neofetch':
            fast_fetch.execute()

        elif answer == 'sudo shutdown' or answer == 'shutdown':
            shutdown.execute(answer)

        elif answer == 'sudo reboot' or answer == 'reboot':
            reboot.execute(answer)

        elif answer == 'exit':
            break

        else:
            print('command not found')
            continue