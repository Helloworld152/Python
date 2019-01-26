from requests import *

r = get("http://www.baidu.com")
r.encoding = 'utf-8'
print(r.status_code, r.text)
