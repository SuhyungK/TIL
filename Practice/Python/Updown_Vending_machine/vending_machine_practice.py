print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.
    
    # 1.금액 넣기

    if money > 0:
        budget += money
        print(f'현재 누적 금액은 {budget}원입니다.')
    elif money < 0:
        print('금액은 1원 이상 넣어주세요.')
        continue
    else:
        break

    # 2.메뉴 출력
    
    if budget < min(costs):
        print(f'{budget}으로 구매 가능한 메뉴가 없습니다.')
        break
    else:
        print('[Menu]' + '\n' + f'{budget}으로 구매 가능한 메뉴는 다음과 같습니다.')

        for idx, cost in enumerate(costs):
            if budget > cost:
                print(f'{idx + 1}. {menus[idx]} {costs[idx]}원')
    
    # 3.메뉴 선택
    
    while True:
        num = int(input('구매하실 메뉴의 번호를 입력하세요. '))

        if costs[num - 1] > budget or costs[num -1] == 'Null':
            print('구매할 수 없는 메뉴입니다.')
        else:
            break

    # 4.거스름돈 반환

    print(f'{menus[num - 1]}를 구매하셨습니다.')
    print(f'거스름돈은 {budget - costs[num - 1]}원입니다. 감사합니다.')
    break


