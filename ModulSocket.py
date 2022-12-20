import socket
portList = []
bannerList = []
fp = open("ip.txt", "r")
IPs = fp.read()
fp.close()
for ip in IPs.splitlines():
    print(ip)
    for port in range(1233,1235):
        try:
            soket = socket.socket()
            soket.connect((str(ip), int(port)))
            banner = soket.recv(1024)
            bannerList.append(str(banner))
            portList.append(str(port))
            soket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("The system might be a Linux or Network hardware.")
                log = str(ip)+"\n"
                fp = open("linux.txt", "a")
                fp.write(log)
                fp.close()
        except:
            pass
    print(portList)
