import requests
import re
url = 'http://natas1.natas.labs.overthewire.org'
user ='natas1'
passwd ='gtVrDuiDfck831PqWsLEZy5gyDz1clto'

r = requests.get(url,auth=(user,passwd))
content = r.text
#print(content)
passwd = re.findall('The password for natas2 is (.*) ',content)[0]

print(passwd)

