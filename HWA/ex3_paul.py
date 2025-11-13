# HW3當日菜單
CoC = eval(input("Please input Coffee Cost: "))
Tax = eval(input("Please input Tax in % (5 for 5%): "))

# 餐點價格
CoK = CoC * 2
CoB = CoC * 3
CoS = CoC * 8

# 欄位格數            6      5
# ==== FJUIM's =================
# | # | Item      | Cost | TIC |
# | 1 | Coffee    | 1.0  | 1.0 |
# | 2 | Chicken   | 2.0  | 2.0 |
# | 3 | Burger    | 3.0  | 3.0 |
# | 4 | Steak     | 8.0  | 8.1 |      >> 當價格為一位數 -> 欄位數: 6 + 5
# ==============================      >> 當價格為兩位數 -> 欄位數: 6 + 6
#                                     >> 3 -> 欄位數: 7 + 7

# 先定義欄位的最小長度
LenC = 6  # Cost 欄位
LenT = 5  # TIC 欄位

# 依照Steak的價格位數來進行排版 -> 當你的最貴餐點為一位數(1~9) 那他的欄位格數必定為6
LenST = len(str(int(CoS)))

if LenST > 1:
    LenC = LenST + 4
    LenT = LenST + 4

# 第一行輸出
print("==== FJUIM's ===", end="")
print("=" * (LenC + LenT + 3))

# 第二行輸出
print("| # | Item      | Cost", end="")
print(" " * (LenC - 5), end="")  # 補Cost字樣後面的空格
print("| TIC", end="")
print(" " * (LenT - 4), end="")  # 補TIC字樣後面的空格
print("|")

# 第三行輸出
print("| 1 | Coffee    | ", end="")
print(f"{CoC:<{LenC - 1 }.1f}| {CoC * ((100 + Tax) / 100):<{LenT - 1}.1f}|")

# 第四行輸出
print("| 2 | Chicken   | ", end="")
print(f"{CoK:<{LenC - 1 }.1f}| {CoK * ((100 + Tax) / 100):<{LenT - 1}.1f}|")

# 第五行輸出
print("| 3 | Burger    | ", end="")
print(f"{CoB:<{LenC - 1 }.1f}| {CoB * ((100 + Tax) / 100):<{LenT - 1}.1f}|")

# 第六行輸出
print("| 4 | Steak     | ", end="")
print(f"{CoS:<{LenC - 1 }.1f}| {CoS * ((100 + Tax) / 100):<{LenT - 1}.1f}|")

# 最後行收尾
print("=" * (LenT + LenC + 19))
