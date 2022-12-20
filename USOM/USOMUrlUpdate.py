import requests

response = requests.get("https://www.usom.gov.tr/url-list.txt", verify=False) #ssl verify false
dosya = open("USOM/usom.txt", "w")
dosya.write(str(response.content))
dosya.close()

#usom url-list'i güncellemek için çalıştır.