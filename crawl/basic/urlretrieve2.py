# urlretrieve

import urllib.request as req

# 이미지, 문서 가져오기

# 가져올 url 지정
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEyMTNfMjM2%2FMDAxNjM5NDA0OTUyMDYx.OAJcAWuJpG9R0plSybTH7_i3-IR8Mwi9JIIguhTNgHcg.wwNDvcEnRy_DZgLVagbDoUEc0ESvOt8x53gDhrT4N-sg.JPEG.goodnonz%2FB612_20211116_165359_260.jpg&type=ofullfill340_600"
doc_url = "https://www.naver.com"

# 저장할 파일명 지정
save_img = "d:\\dog.png"
save_doc = "d:\\naver.html"

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
