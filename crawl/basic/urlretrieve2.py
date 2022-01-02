# urlretrieve

import urllib.request as req

# 이미지, 문서 가져오기

# 가져올 url 지정
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEwMjhfMjg3%2FMDAxNjM1MzQ3ODMyNDc4.syy6b78iLjir6m3pajtZSCiEsxLp4pIou4D9_Z3UeuMg.ihYW9C_vKvRClt1BJkMc2t9pZMAYZ03OdjwiE3h8nvQg.PNG.4644khj%2Fimage.png&type=a340"
doc_url = "https://www.naver.com"

# 저장할 파일명 지정
save_img = "c:\\cloud.png"
save_doc = "c:\\naver.html"

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
