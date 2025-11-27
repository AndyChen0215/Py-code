#   *
#  ***
# *****
#  ***
#   *

n = int(input("請輸入半邊層數："))

# 上半部 (包含中間最長的一行)
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 下半部 (從 n-1 開始倒數)
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)