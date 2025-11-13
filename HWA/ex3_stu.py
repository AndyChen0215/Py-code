# 餐點價格
cof = eval(input("PPlease input Coffee Cost:"))
chi = cof * 2
bur = cof * 3
ste = cof * 8
tax = eval(input("Please input Tax in % (5 for 5%):")) * 0.01


row1 = f"| {'#':<2}|{'Item':<8}| {'Cost':<7}|{'TIC':^7} |"
row2 = f"| {1:<2}|{'Coffee':<8}| {cof:<7.1f}|{cof+(cof*tax):^7.1f}{'|':>2}"
row3 = f"| {2:<2}|{'Chicken':<8}| {chi:<7.1f}|{chi+(chi*tax):^7.1f}{'|':>2}"
row4 = f"| {3:<2}|{'Burger':<8}| {bur:<7.1f}|{bur+(bur*tax):^7.1f}{'|':>2}"
row5 = f"| {4:<2}|{'Steak':<8}| {ste:<7.1f}|{ste+(ste*tax):^7.1f}{'|':>2}"
max_len = max(len(row2), len(row3), len(row4), len(row5))

print("======FJUIM's" + "=" * (max_len - len("======FJUIM's")))
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print("=" * (max_len))
