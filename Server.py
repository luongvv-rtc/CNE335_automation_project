import os
import paramiko

#class Server:
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
        self.username = username
        self.command = command

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.key = paramiko.RSAKey.from_private_key_file(key_pair)


    def ping(self):
        # TODO - Use os module to ping the server
        if os.system(f'ping -n 5 {self.server_ip}') == 0:
            return True
        else:
            return False


    def upgrade(self):
        # https://blog.ruanbekker.com/blog/2018/04/23/using-paramiko-module-in-python-to-execute-remote-bash-commands/
        self.ssh.connect(hostname=self.server_ip, username=self.username, pkey=self.key)

        # Execute Command
        stdin, stdout, stderr = self.ssh.exec_command(self.command)
        #for line in stdout.read().splitlines():
        #    print(line)
        line = stdout.readline()
        while line:
            print(line)
            line = stdout.readline()
        print(stderr.read().decode())
        # Disconnect
        self.ssh.close()