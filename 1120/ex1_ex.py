# 洗牌法
import random

# 1. 準備好 0-9 的所有數字 (就像一副牌)
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 2. 洗牌 (原地打亂順序)
random.shuffle(digits)

# 3. 發牌 (取出前 4 張)
# digits[:4] 代表取出索引 0 到 3 的元素
answer_list = digits[:4]

# 4. 組合字串
ans = "".join(answer_list)

print(f"答案是: {ans}")


# list 檢查法
import random

# 1. 準備一個空籃子 (列表)
answer_list = []

# 2. 當籃子還沒滿 4 個球，就繼續撿
while len(answer_list) < 4:
    
    # 3. 隨機撿一個 0-9 的數字
    num = str(random.randint(0, 9))
    
    # 4. (關鍵) 檢查籃子裡是不是「還沒有」這個數字
    if num not in answer_list:
        answer_list.append(num)  # 沒重複才放進去

# 5. 組合字串
ans = "".join(answer_list)

print(f"答案是: {ans}")


# 字串串接法
import random

# 準備一個空字串
ans = ""

# 當字串長度還不到 4，就繼續找
while len(ans) < 4:
    
    # 隨機產生一個數字
    num = str(random.randint(0, 9))
    
    # 4. 檢查這個數字是否「不在」字串裡
    if num not in ans:
        ans = ans + num

print(f"答案是: {ans}")


a = set()
b = set([1,2,3,4,5,1,2,3,4,5])
c = set({'x':1,'y':2,'z':3})
d = set('hello')
print(a)   # set()
print(b)   # {1, 2, 3, 4, 5}  只留下不重複的部分
print(c)   # {'x', 'y', 'z'}  如果是字典，只保留鍵
print(d)   # {'l', 'o', 'h', 'e'}  只留下不重複的部分