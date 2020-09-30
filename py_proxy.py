import re

import requests

headers = {'Host': 'www.my-proxy.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0', 
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3', 
 'Connection': 'keep-alive', 'Referer': 'https://www.my-proxy.com/free-proxy-list-1.html', 
'Upgrade-Insecure-Requests': '1'}

page = 0
all_proxy_adress = []

while page < 10 :
    page += 1
    r = requests.get('https://www.my-proxy.com/free-proxy-list-' + str(page) + '.html', headers=headers)
    r.encoding = 'UTF8'
    data = r.text
    n = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{2,4}', data)
    all_proxy_adress.extend(n)
    
print(all_proxy_adress)
print(len(all_proxy_adress))
