numbers = input("請輸入數字(以空格隔開)\n").split(" ")

# 建立空列表
odds = []  # 存放奇數
evens = []  # 存放偶數

# 使用 for 迴圈遍歷列表
for num_str in numbers:

    # 先將str型態轉換為int
    num = int(num_str)

    # 判斷邏輯：檢查除以 2 的餘數
    if num % 2 == 0:
        # 餘數為 0，代表是偶數 -> 加入 evens 列表
        evens.append(num)
    else:
        # 餘數不為 0，代表是奇數 -> 加入 odds 列表
        odds.append(num)

# 印出結果
print(f"奇數：{odds}")
print(f"偶數：{evens}")
