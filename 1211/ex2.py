import random

options = ["剪刀", "石頭", "布"]

print("--- 猜拳遊戲 (輸入 quit 離開) ---")

while True:
    user_input = input("\n請出拳 (剪刀/石頭/布)：")
    
    if user_input == "quit":
        print("遊戲結束")
        break
        
    if user_input not in options:
        print("輸入錯誤，請重新輸入")
        continue
        
    computer_choice = random.choice(options)
    print(f"電腦出：{computer_choice}")
    
    # 判斷勝負
    if user_input == computer_choice:
        print("結果：平手！")
    elif (user_input == "剪刀" and computer_choice == "布") or \
         (user_input == "石頭" and computer_choice == "剪刀") or \
         (user_input == "布" and computer_choice == "石頭"):
        print("結果：你贏了！")
    else:
        print("結果：你輸了...")