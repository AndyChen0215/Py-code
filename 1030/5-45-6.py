def calculate_tax(income):
    # 宣告一個變數來儲存計算結果
    tax = 0

    # 使用 if...elif...else 鏈來判斷所得區間
    # 順序必須由小到大
    
    if income <= 0:
        # 處理負數或 0 的情況
        tax = 0
    elif income <= 590000:
        # 區間 1：0 ~ 590,000
        # 稅率 5%, 累進差額 0
        rate = 0.05
        deduction = 0
        tax = income * rate - deduction
        
    elif income <= 1330000:
        # 區間 2：590,001 ~ 1,330,000
        # 稅率 12%, 累進差額 41,300
        rate = 0.12
        deduction = 41300
        tax = income * rate - deduction

    elif income <= 2660000:
        # 區間 3：1,330,001 ~ 2,660,000
        # 稅率 20%, 累進差額 147,700
        rate = 0.20
        deduction = 147700
        tax = income * rate - deduction
        
    elif income <= 4980000:
        # 區間 4：2,660,001 ~ 4,980,000
        # 稅率 30%, 累進差額 413,700
        rate = 0.30
        deduction = 413700
        tax = income * rate - deduction
        
    else:
        # 區間 5：4,980,001 以上
        # 稅率 40%, 累進差額 911,700
        rate = 0.40
        deduction = 911700
        tax = income * rate - deduction

    # 稅金四捨五入到整數
    return round(tax)

try:
    # 1. 提示使用者輸入
    net_income = int(input("請輸入您的全年綜合所得淨額 (新台幣)："))

    # 2. 呼叫函式計算
    final_tax = calculate_tax(net_income)

    # 3. 輸出結果
    print(f"您的所得淨額為：{net_income} 元")
    print(f"經計算，您的全年應納稅額為：{final_tax} 元")

except ValueError:
    print("輸入錯誤：請務必輸入一個有效的整數金額。")