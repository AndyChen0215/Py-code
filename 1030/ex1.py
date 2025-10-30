a,b,c = eval(input())

if a <= 0 or b <= 0 or c <= 0:
    print('邊長必須是正數')

# 檢查是否為三角形
elif (a + b > c) and (a + c > b) and (b + c > a):
    # 正三角形
    if a == b and b == c:
        print('正三角形')

    # 等腰三角形
    elif a == b or b == c:
        print('等腰三角形')
        
    # 不等邊三角形
    else:
        print('不等邊三角形')
else:
    print('無法構成三角形')