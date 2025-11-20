import random

print("--- 1A2B 猜數字遊戲 ---")

answer_list = random.sample("0123456789", 4)
ans = "".join(answer_list)

# ans = '5431'

print(f"(測試用答案: {ans})")

# guess_count = 0 # 用來計算猜了幾次
while 1:
    
    # 取得使用者的猜測
    guess = input("\n請猜一個 4 位數 (數字不重複)：")
    # guess_count = guess_count + 1

    # 使用者輸入驗證
    if len(guess) != 4:
        print("輸入錯誤：長度必須是 4 個字元。")
        continue  # 'continue' 會跳過這次迴圈，回到 input 重新猜

    if not guess.isdigit():
        print("輸入錯誤：只能包含數字。")
        continue

    if len(set(guess)) != 4:
        print("輸入錯誤：數字不能重複。")
        continue

    #    A 和 B 的計數器必須放在迴圈內，這樣「每一次」猜測都會重新歸零
    a_count = 0
    b_count = 0
    
    #    使用 for 迴圈來「迭代」4 個位置 (i 會依序是 0, 1, 2, 3)
    for i in range(4):
        # 1. 檢查 'A' (位置對，數字也對)
        if guess[i] == ans[i]:
            a_count = a_count + 1
            
        # 2. 檢查 'B' (位置錯，但數字對)
        elif guess[i] in ans:
            b_count = b_count + 1
            
    # 顯示提示
    print(f"{guess} -> 結果是: {a_count}A{b_count}B")

    # 判斷是否勝利
    if a_count == 4:
        print("-" * 30)
        print(f"恭喜！你猜對了！ 答案就是 {ans}。")
        # print(f"你總共猜了 {guess_count} 次。")
        
        # 'break' 用來跳出 while True 迴圈
        break 

print("--- 遊戲結束 ---")