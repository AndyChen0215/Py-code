x = 31
binx = bin(x)[2:]  # 去掉 '0b' 前綴
octx = oct(x)[2:]
hexx = hex(x)[2:]

# 中文字無法很完美的對齊
print(f'{"二進位":>10s}' f'{"八進位":>10s}' f'{"十六進位":>10s}')
print(f"{binx:>10s}" f"{octx:>10s}" f"{hexx:>10s}")

# 使用英文字對齊
print(f'{"bin":>10s}' f'{"oct":>10s}' f'{"hex":>10s}')
print(f"{binx:>10s}" f"{octx:>10s}" f"{hexx:>10s}")