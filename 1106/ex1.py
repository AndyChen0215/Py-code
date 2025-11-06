import random

secret_number = random.randint(1, 100)

print(f"(測試用，秘密數字是: {secret_number})")

print("--- 猜數字遊戲開始 (1-100) ---")

while True:

    # 讓使用者輸入猜測
    guess = eval(input("請猜一個數字："))

    # 檢查數字是否在 1-100 範圍內
    if guess < 1 or guess > 100:
        print("範圍錯誤，請輸入 1 到 100 之間的數字。")

    elif guess > secret_number:
        print("太大了！再猜低一點。")

    elif guess < secret_number:
        print("太小了！再猜高一點。")

    else:  # (guess == secret_number)
        print(f"你猜對了！答案就是 {secret_number}")
        break


print("--- 遊戲結束 ---")
