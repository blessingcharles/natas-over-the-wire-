import requests
import re
url = 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'
user ='natas3'
passwd ='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

r = requests.get(url,auth=(user,passwd))
content = r.text
#print(content)
passwd = re.findall('natas4:(.*)',content)[0]

print(passwd)

