# for i in range(3):
#     for j in range(3):
#         print(j, end=" ")
# print()

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # * * *


# break, continue

i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")  # 1 2 3 4
    i += 1

print()

i = 1
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")  # 2 4 6 8 10
