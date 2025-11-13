import math

# --- 取得輸入並計算 ---
coffee_price = float(input("Please input Coffee Cost: "))
tax_percent = float(input("Please input Tax in % (5 for 5%): "))

tax_rate = tax_percent / 100.0

# 售價 (Cost)
cost_coffee = coffee_price
cost_chicken = coffee_price * 2
cost_burger = coffee_price * 3
cost_steak = coffee_price * 8

# 含稅價 (TIC)
tic_coffee = cost_coffee * (1 + tax_rate)
tic_chicken = cost_chicken * (1 + tax_rate)
tic_burger = cost_burger * (1 + tax_rate)
tic_steak = cost_steak * (1 + tax_rate)

# --- 格式化所有欄位內容 (前後加空白) ---

# 標頭 (Header)
header_num = " # "
header_item = " Item "
header_cost = " Cost "
header_tic = " TIC "

# 欄位 1: #
data_num_1 = " 1 "
data_num_2 = " 2 "
data_num_3 = " 3 "
data_num_4 = " 4 "

# 欄位 2: Item
data_item_1 = " Coffee "
data_item_2 = " Chicken "
data_item_3 = " Burger "
data_item_4 = " Steak "

# 欄位 3: Cost (格式化為 .1f 並加上前後空白)
data_cost_1 = f" {cost_coffee:.1f} "
data_cost_2 = f" {cost_chicken:.1f} "
data_cost_3 = f" {cost_burger:.1f} "
data_cost_4 = f" {cost_steak:.1f} "

# 欄位 4: TIC (格式化為 .1f 並加上前後空白)
data_tic_1 = f" {tic_coffee:.1f} "
data_tic_2 = f" {tic_chicken:.1f} "
data_tic_3 = f" {tic_burger:.1f} "
data_tic_4 = f" {tic_steak:.1f} "

# --- 3. (關鍵) 計算「剛剛好」的欄寬 ---
# 找出每一欄中，最長的字串長度

W_num = max(
    len(header_num),
    len(data_num_1),
    len(data_num_2),
    len(data_num_3),
    len(data_num_4),
)
W_item = max(
    len(header_item),
    len(data_item_1),
    len(data_item_2),
    len(data_item_3),
    len(data_item_4),
)
W_cost = max(
    len(header_cost),
    len(data_cost_1),
    len(data_cost_2),
    len(data_cost_3),
    len(data_cost_4),
)
W_tic = max(
    len(header_tic),
    len(data_tic_1),
    len(data_tic_2),
    len(data_tic_3),
    len(data_tic_4),
)

# --- 4. 計算總寬度 ---
# 總寬度 = 5個'|' + 各欄寬度
total_width = 1 + W_num + 1 + W_item + 1 + W_cost + 1 + W_tic + 1

# --- 5. 使用 f-string 的「變數寬度」來排版 ---

# (a) 首行
header_prefix = "==== FJUIM's "
header_padding = "=" * (total_width - len(header_prefix))
print(f"{header_prefix}{header_padding}")

# (b) 表頭 (全部置中)
# f"{variable:^{width_variable}}" -> 變數置中於「變數寬度」
print(
    f"|{header_num:^{W_num}}|{header_item:^{W_item}}|{header_cost:^{W_cost}}|{header_tic:^{W_tic}}|"
)

# (c) 表內 (Item靠左<, 數字靠右>)
print(
    f"|{data_num_1:^{W_num}}|{data_item_1:<{W_item}}|{data_cost_1:>{W_cost}}|{data_tic_1:>{W_tic}}|"
)
print(
    f"|{data_num_2:^{W_num}}|{data_item_2:<{W_item}}|{data_cost_2:>{W_cost}}|{data_tic_2:>{W_tic}}|"
)
print(
    f"|{data_num_3:^{W_num}}|{data_item_3:<{W_item}}|{data_cost_3:>{W_cost}}|{data_tic_3:>{W_tic}}|"
)
print(
    f"|{data_num_4:^{W_num}}|{data_item_4:<{W_item}}|{data_cost_4:>{W_cost}}|{data_tic_4:>{W_tic}}|"
)

# (d) 表尾
print("=" * total_width)
