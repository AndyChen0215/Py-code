import math

s = eval(input())

h = ((math.sqrt(3)) / 2) * s
area = ((math.sqrt(3)) / 4) * math.pow(s, 2)

print("高 = " f"{h}")
print("面積 = " f"{area}")


# 如果不使用 import math 的寫法
print("\n不使用math套件")

h = ((3**0.5)/2) * s
area = ((3**0.5)/4) * (s*s)

print("高 = " f'{h}')
print("面積 = " f'{area}')