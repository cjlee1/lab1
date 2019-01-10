import requests
print(requests.__version__)

#r = requests.get("https://www.google.com")
#print(r.status_code)
#print(r.text)

#print(dir(r))

a = requests.get("https://raw.githubusercontent.com/cjlee1/lab1/master/script3.py")

print(a.text)