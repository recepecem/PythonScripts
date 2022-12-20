import requests
fp = open("fuzzer.txt", "r")
content = fp.read()
fp.close()

for i in content.split("\n"):
    print(i)
    url= "http://example.com"+str(i)
    result = requests.get(url=url)
    if "200" in str(result.status_code):
        print("found a directory or file")
    else:
        print("no such file or directory")
