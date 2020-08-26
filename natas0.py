import requests
import re
url = 'http://natas0.natas.labs.overthewire.org'
user ='natas0'
passwd ='natas0'

r = requests.get(url,auth=(user,passwd))
content = r.text

passwd = re.findall('The password for natas1 is (.*)',content)[0]

print(passwd)

