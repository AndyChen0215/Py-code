a = eval(input())
b = eval(input())
c = eval(input())

ans = (4/(3*(a+34)))-9*(a+b*c)+((3+3*(2+a))/(a+3*b))

print(ans)

# 拆開來的解法

term1 = 4 / (3 * (a + 34))
term2 = 9 * (a + b * c)
term3 = (3 + 3 * (2 + a)) / (a + 3 * b)

ans = term1 - term2 + term3

print(ans)