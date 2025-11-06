import random


def get_turn_result():
    dice_rolls = []  # 用來儲存五次骰子的結果
    total_score = 0  # 用來累加總分

    for i in range(5):
        # 產生 1 到 6 之間的隨機整數
        roll = random.randint(1, 6)

        # 將結果存入列表
        dice_rolls.append(roll)

        # 如果投出骰子的數值是 3 的話，計為 0
        if roll == 3:
            total_score = total_score + 0
        else:
            # 其它數值的話，計為該數值
            total_score = total_score + roll

    # 回傳這回合的結果
    return dice_rolls, total_score


# 投五次骰子
player_rolls, player_score = get_turn_result()

# 為電腦投五次骰子
computer_rolls, computer_score = get_turn_result()

# --- 列印雙方結果 ---
print("--- 遊戲開始！分數低者獲勝 ---")
print(f"你擲出的骰子是: {player_rolls}")
print(f"你的總分為: {player_score}")
print("-" * 25)  # 分隔線
print(f"電腦擲出的骰子是: {computer_rolls}")
print(f"電腦的總分為: {computer_score}")
print("-" * 25)

# --- 判斷獲勝方 ---
print("--- 遊戲結果 ---")
if player_score < computer_score:
    print(f"恭喜！你獲勝了！ ({player_score} 分 < {computer_score} 分)")
elif computer_score < player_score:
    print(f"可惜，電腦獲勝。 ({computer_score} 分 < {player_score} 分)")
else:
    print(f"平手！雙方的分數都是 {player_score} 分。")
