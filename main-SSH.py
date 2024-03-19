# CNE335 Winter 2024
# Student name: Van Vuong
# Automate SSH Assignment

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Van")

if __name__ == '__main__':
    print_program_info()
    server = Server('35.93.122.103', 'C:\KP_Web.pem')

    # run upgrade and update command
    command = 'sudo apt update && sudo apt upgrade -y'
    # Call Ping and print results
    if server.ping():
        print("Updating server...")
        # server.run_command(command)
        ssh_result = server.run_command(command)

