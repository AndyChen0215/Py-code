import random

secret_number = random.randint(1, 100)

print(f"(測試用，秘密數字是: {secret_number})")

print("遊戲開始")

while True:

    guess = eval(input("請猜一個數字"))

    if guess < 1 or guess > 100:
        print("範圍錯誤")

    elif guess < secret_number:
        print("數字太小")

    elif guess > secret_number:
        print("數字太大")

    elif guess == secret_number:
        print("猜對了")
        break

print("遊戲結束")
