# urlretrieve

import urllib.request as req

#  좋아하는 사진 저장하기 / python.org 사이트 저장

img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEyMTRfODcg%2FMDAxNjM5NDY5NjE4MTQ2.-rcqagKxyVTfajGcFKJoFyl2RVw_4GPXjz7Qyy8JLyog.vSKJ5MBfDQpN0vyLudXJ-cg-JWgLnp4EvmGOuRV9paYg.JPEG.ped95%2FDSC02499.JPG&type=a340"
doc_url = "http://python.org"

save_img = "d:\\cat.png"
save_doc = "d:\\python.html"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
    file2, header2 = req.urlretrieve(doc_url, save_doc)
except Exception as e:
    print(e)
else:
    print(header1)
    print("-" * 50)
    print(header2)
    print()

    print("Filename : {}".format(file1))
    print("Filename : {}".format(file2))
