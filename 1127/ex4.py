# *****
#  ***
#   *

n = int(input("請輸入層數："))
# range(開始, 結束, -1) 代表倒數
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)