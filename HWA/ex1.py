# 2025 年個人免稅額
PERSONAL_EXEMPTION = 350000

# 級距門檻
LIMIT_1 = 590000
LIMIT_2 = 1330000
LIMIT_3 = 2660000
LIMIT_4 = 4980000

# 稅率
RATE_1 = 0.05
RATE_2 = 0.12
RATE_3 = 0.20
RATE_4 = 0.30
RATE_5 = 0.40

# 預先算好「每一級距全滿」時的稅金
# 這是解題的關鍵，避免重複計算
TAX_BRACKET_1_FULL = LIMIT_1 * RATE_1  # 29,500
TAX_BRACKET_2_FULL = (LIMIT_2 - LIMIT_1) * RATE_2  # 88,800
TAX_BRACKET_3_FULL = (LIMIT_3 - LIMIT_2) * RATE_3  # 266,000
TAX_BRACKET_4_FULL = (LIMIT_4 - LIMIT_3) * RATE_4  # 696,000


def calculate_progressive_tax(nic):
    total_tax = 0

    # 已知所得稅的課稅級距
    if nic <= 0:
        # 當NIC為零或負數時，則該年不用繳交所得稅。
        total_tax = 0

    elif nic <= LIMIT_1:
        # 落在第 1 級距
        # 59萬元(含)以下者，課徵所得淨額的5％
        total_tax = nic * RATE_1

    elif nic <= LIMIT_2:
        # 落在第 2 級距
        # (第 1 級全繳) + (第 2 級的部份)
        total_tax = TAX_BRACKET_1_FULL + (nic - LIMIT_1) * RATE_2

    elif nic <= LIMIT_3:
        # 落在第 3 級距
        # (第 1 級全繳) + (第 2 級全繳) + (第 3 級的部份)
        total_tax = TAX_BRACKET_1_FULL + TAX_BRACKET_2_FULL + (nic - LIMIT_2) * RATE_3

    elif nic <= LIMIT_4:
        # 落在第 4 級距
        total_tax = (
            TAX_BRACKET_1_FULL
            + TAX_BRACKET_2_FULL
            + TAX_BRACKET_3_FULL
            + (nic - LIMIT_3) * RATE_4
        )

    else:
        # 落在第 5 級距
        total_tax = (
            TAX_BRACKET_1_FULL
            + TAX_BRACKET_2_FULL
            + TAX_BRACKET_3_FULL
            + TAX_BRACKET_4_FULL
            + (nic - LIMIT_4) * RATE_5
        )

    return total_tax


try:
    # 從使用者處取得全年綜合所得IC
    ic = int(input("請輸入您的全年綜合所得 (IC)："))

    # 所得淨額NIC = 綜合所得IC – 個人免稅額
    nic = ic - PERSONAL_EXEMPTION

    print("-" * 30)
    print(f"您的綜合所得 (IC): {ic: ,} 元")
    print(f"您的所得淨額 (NIC): {nic: ,} 元")

    # 計算應繳稅額
    total_tax = calculate_progressive_tax(nic)

    # 輸出... (取整數)
    final_tax = round(total_tax)

    # 輸出... 每月平均可支配所得
    # 可支配所得 = 總收入 - 稅
    disposable_income = ic - final_tax
    monthly_avg = round(disposable_income / 12)

    print("-" * 30)
    print(f"您 2025 年需要繳交的所得稅為： {final_tax: ,} 元")
    print(f"扣稅後每月平均可支配所得為： {monthly_avg: ,} 元")


except ValueError:
    print("輸入錯誤：請務必輸入一個有效的整數金額。")
