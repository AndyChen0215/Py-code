numbers = [33, 12, 56, 7, 99, 44, 18]

# 建立空列表
odds = []  # 存放奇數
evens = []  # 存放偶數

# 使用 for 迴圈遍歷列表
for num in numbers:

    # 判斷邏輯：檢查除以 2 的餘數
    if num % 2 == 0:
        # 餘數為 0，代表是偶數 -> 加入 evens 列表
        evens.append(num)
    else:
        # 餘數不為 0，代表是奇數 -> 加入 odds 列表
        odds.append(num)

# 印出結果
print(f"原始列表：{numbers}")
print(f"偶數列表：{evens}")
print(f"奇數列表：{odds}")
