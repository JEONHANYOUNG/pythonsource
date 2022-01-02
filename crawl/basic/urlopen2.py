import urllib.request as req

try:
    best_url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb#pageNum%%2"

    response = req.urlopen(best_url)
    contents = response.read().decode("euc-kr")
except Exception as e:
    print(e)
else:
    print("header :{} ".format(response.info()))
    print(contents[:4000])
