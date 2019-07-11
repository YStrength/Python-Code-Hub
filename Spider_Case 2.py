#爬图片
import requests
import os
url = "address"
root = "D://dirname//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(path)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("Successful save")
    else:
        print("File has existed")
except:
    print("Fail")