import csv

list1 = [1, 2, 3, 4, 5]

with open("./sample3.csv", "w") as f:
    wt = csv.writer(f)

    wt.writerow(list1)
