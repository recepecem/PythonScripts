import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.10.10.10", username= "msfadmin", password= "msfadmin")
stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd")

for i in stdout.read().decode('ascii').split("\n"):
    if int(str(i).split(":")[2]) == 0:
        print("User with UID 0: ", str(i).split(":")[0])
