# CNE335 Winter 2024
# Student name: Van Vuong
# Automate SSH Assignment

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Van")


if __name__ == 'main':
    print_program_info()
    # Server IP, key_pair and username:
    server_ip = '35.93.122.103'
    key_pair = 'D:\Personal\OneDrive\PERSONAL\Documents\US Doc\Luong\RTC\BAS\Winter 2024\CNE 335 - Network programing II Python\KP_Web.ppk'
    username = 'ubuntu'

    # run upgrade and update command
    command = 'sudo apt update && sudo apt upgrade -y'
    server = Server(server_ip, key_pair, username, command)

    # Call Ping and print results
    print(server.ping())
    print("Updating server...")
    ssh_result = server.upgrade
    print(ssh_result)