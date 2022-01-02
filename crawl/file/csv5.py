import csv

list1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

with open("./sample4.csv", "w", newline="") as f:
    wt = csv.writer(f)

    for item in list1:
        wt.writerow(item)

    # 리스트를 한꺼번에 저장
    # wt.writerows(list1)
