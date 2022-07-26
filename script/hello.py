import paramiko
import os
import sys
import json

def sudo_user_access(users_file_path,hosts_file_path,pem_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(users_file_path)
    print(hosts_file_path)
    with open(users_file_path) as f:
        users = f.readlines()
    with open(hosts_file_path) as f:
        hosts = f.readlines()
    privkey = paramiko.RSAKey.from_private_key_file(pem_file)
    print(users)
    print(hosts)
    print(privkey)
#     for host_name in hosts:
#         host_name = host_name.replace("\n","")
#         print(host_name)
#         print("Connecting to ssh using hostname " + host_name)
#         try:
#             ssh.connect(hostname=host_name, username='ec2-user', pkey=privkey)
#         except paramiko.AuthenticationException:
#             print("Authentication failed when connecting to" + ip)
#             continue
#         print("Successfully connected to ssh using hostname "+host_name)
#         for user_name in users:
#             user_name = user_name.replace("\n","")
#             stdin, stdout, stderr = ssh.exec_command("sudo usermod –aG wheel "+user_name)
#             print("successfully given root permission for "+user_name)
#         ssh.exec_command("exit")
#         print("Disconnected from ssh connection with hostname "+host_name)
    #ssh.exec_command("logout")
    
if( len(sys.argv) != 4):
    print("please pass users_file_path and hosts_file_path")
    exit(1)

users_file_path = sys.argv[1]
hosts_file_path = sys.argv[2]
pem_file = sys.argv[3]


sudo_user_access(users_file_path,hosts_file_path,pem_file)
