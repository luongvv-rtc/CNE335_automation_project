import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    # Code for Server Ping Assignment
    # def __init__(self, server_ip):
    #     # TODO -
    #     self.server_ip = server_ip
    #
    # def ping(self):
    #     # TODO - Use os module to ping the server
    #     result = os.system(f'ping -n 5 {self.server_ip}')
    #     return result

    # Code for Automated SSH Assignment

class Server:

    def __init__(self, server_ip, key_pair, username, command):
        # TODO -
        self.server_ip = server_ip
        self.key_pair = key_pair
        self.username = username
        self.command = command


    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system(f'ping -n 5 {self.server_ip}')
        return result


    def upgrade(self):
        # https://blog.ruanbekker.com/blog/2018/04/23/using-paramiko-module-in-python-to-execute-remote-bash-commands/
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.key = paramiko.RSAKey.from_private_key_file(self.key_pair)
        self.ssh.connect(hostname=self.server_ip, username=self.username, pkey=self.key)

        # Execute Command
        stdin, stdout, stderr = self.ssh.exec_command(self.command)
        for line in stdout.read().splitlines():
            print(line)

        # Disconnect
        self.ssh.close()