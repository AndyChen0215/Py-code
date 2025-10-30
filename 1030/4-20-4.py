import math

# 讀使用者輸入x1,y1
point1 = input().split(" ")
x1 = float(point1[0])
y1 = float(point1[1])

# 讀使用者輸入x2,y2
point2 = input().split(" ")
x2 = float(point2[0])
y2 = float(point2[1])

# 轉換成弧度
x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)


# 公式如下
# radius = 6371
# d = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2))

# 公式拆分
# f1 = sin(x1) * sin(x2)
# f2 = cos(x1) * cos(x2) * cos(y1-y2)
# value = f1 + f2
# arc_cos = acos(value)
# d = radius * arc_cos

# 實作
radius = 6371
f1 = math.sin(x1_rad) * math.sin(x2_rad)
f2 = math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad)
value = f1 + f2
arc_cos = math.acos(value)
d = radius * arc_cos

print(f"The dis... points is {d}")
