age = input('你今年幾歲呢?')


drive = input('你有開過車嗎?')
if drive != '有' and drive != '沒有':
    print('只能輸入有/沒有')
    raise SystemExit

age = int(age)
if age >= 18: 
    if drive == '有':
        print('水歐')
    elif drive == '沒有':
        print('幾歲了?沒見過世面?')
elif age < 18:
    if drive == '有':
        print('毛沒長齊?開車很屌逆?')
    elif drive == '沒有':
        print('很好!很守規矩')
    