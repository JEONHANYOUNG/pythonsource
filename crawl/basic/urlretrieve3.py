# urlretrieve

import urllib.request as req

# 좋아하는 사진 저장하기 / python.org 사이트 저장
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMjhfMjU2%2FMDAxNjExODA3ODgyOTIx.P9kbjq8amWAfA0mNVk0l5fuAod1b5u37DJ0q_y-BrzAg.ZQI0Qw7e4j38ccp22jBZeozbbaRfmqkWyAJPaT6EAzQg.JPEG.soonnye0425%2F10.JPG&type=a340"
doc_url = "http://python.org"

# 저장할 파일명 지정
save_img = "c:\\camera.png"
save_doc = "c:\\python.html"

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
