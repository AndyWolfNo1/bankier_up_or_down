import requests
import time
from random import randint

number = open('num', 'r')
num = number.read()
number.close()
num = int(num)
nume = str(num)


url = 'http://www.bankier.pl/forum/post-zaglosuj'
payload = {'post_id': '44329341', 'vote': 'up',
           'ajax_request': 'true', '_': nume}

r = requests.get(url, params=payload)
#print(num, type(num))
print(r.text)

new_num = num+1
new_number = open('num', 'w+')
new_number.write(str(new_num))
new_number.close()
#time.sleep(randint(0, 10))
#print('wykonano')
