# CNE335 Winter 2024
# Student name: Van Vuong
# Automate Ping Assignment

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Van")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    ec2 = Server('18.236.67.210')
    # TODO - Call Ping method and print the results
    ec2.ping()

