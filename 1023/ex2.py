money = eval(input())

fifty = money // 50
money = money % 50

ten = money // 10
money = money % 10

five = money // 5
money = money % 5

one = money

print(f'{fifty} 'f'{ten} 'f'{five} 'f'{one}')