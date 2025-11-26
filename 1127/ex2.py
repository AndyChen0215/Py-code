n = int(input("請輸入層數："))
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * i
    print(spaces + stars)