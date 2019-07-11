# 爬IP地址
import requests
url = "http://www.ip138.com/ips138.asp?ip="
ip = input()
try:
    r = requests.get(url + ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2500:-2000])
except:
    print("Fail")