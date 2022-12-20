import requests

header = {"X-ApiKeys":"accessKey=[your access key]; secretKey=[your secret key];"}
url = "https://127.0.0.1:8834/scans"
result = requests.get(url=url, headers=header, verify = False)

for i in result.json()["scans"]:
    scan_id = i["id"]
    url = "https://127.0.0.1:8834/scans/" + str(i["id"])
    result = requests.get(url = url, headers = header, verify = False)
    for i in result.json()["hosts"]:
        IP = i['hostname']
        host_id = i['host_id']
        print(IP)
        print(host_id)
        print("=========================================")
        url = "https://127.0.0.1:8834/scans"+str(scan_id)+"/hosts/"+str(host_id)+"/plugins/11936"
        vulnerability = requests.get(url = url, headers = header, verify = False)
        print(vulnerability)






