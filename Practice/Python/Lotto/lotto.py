# 여기에 필요한 모듈을 추가합니다.
import random, json
from datetime import datetime, date

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        self.n = n
        self.number_lines += [sorted(random.sample(range(1,46), 6)) for i in range(self.n)]


    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = self.get_draw_date(draw_number)
        days = ['월', '화', '수', '목', '금', '토', '일']
        _day = date(int(year), int(month), int(day))
        weekday = datetime.weekday(_day)

        print(f"""
==========================================
              제 {draw_number} 회 로또
==========================================
추첨일 : {int(year)}/{int(month):02d}/{int(day):02d} ({days[weekday]})
==========================================
        """)
        for i in range(self.n):
            print(f'{chr(i+65)} : {self.number_lines[i]}')



    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = self.get_lotto_numbers(draw_number)
        same_main_counts, is_bonus = [], []

        for i in range(self.n):
            same_main_counts.append(self.get_same_info(main_numbers, bonus_number,self.number_lines[i])[0])
            is_bonus.append(self.get_same_info(main_numbers, bonus_number,self.number_lines[i])[1])
        
        ranking = []
        for i in range(self.n):
            ranking.append(self.get_ranking(same_main_counts[i], is_bonus[i]))

    

        print(f"""
==========================================
당첨 번호 : {main_numbers} + {bonus_number}
==========================================
        """)

        for i in range(self.n):
            if ranking[i] == -1:
                print(f'{chr(i+65)} : {same_main_counts[i]}개 일치 (낙첨)', end='')
            else:
                print(f'{chr(i+65)} : {same_main_counts[i]}개 일치 ', end='')
                if is_bonus[i]:
                    print('+ 보너스 일치 ',end='')
                print(f'({ranking[i]}등 당첨!)',end='')
            print()
     

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        data = open('data/lotto_' + str(draw_number) + '.json', encoding='UTF-8')
        lotto_data = json.load(data)['drwNoDate']
        year, month, day = lotto_data.split('-')
        
        return year, month, day


    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        data = open('data/lotto_' + str(draw_number) + '.json', encoding='UTF-8')
        lotto_data = json.load(data)
        main_numbers = []
        for k, i in lotto_data.items():
            if k.startswith('drwt'):
                main_numbers.append(i)
        bonus_number = lotto_data['bnusNo']
        
        return sorted(main_numbers), bonus_number


    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False
        for n in range(len(main_numbers)):
            if main_numbers[n] in line:
                same_main_counts += 1
        if bonus_number in line:
            is_bonus = True
        return same_main_counts, is_bonus


    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        rank_system = '65543210'
        ranking = rank_system.find(str(same_main_counts)) + 1
        if ranking == 2 and not is_bonus:
            ranking += 1
        elif ranking >= 6:
            ranking = -1
        return ranking

