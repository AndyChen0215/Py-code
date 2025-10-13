x = 31
binx = bin(x)[2:]  # 去掉 '0b' 前綴
octx = oct(x)[2:]
hexx = hex(x)[2:]


print(f'{"二進位":6s}' f'{"八進位":6s}' f'{"十六進位":6s}')
print(f"{binx:>6s}" f"{octx:>9s}" f"{hexx:>9s}")
