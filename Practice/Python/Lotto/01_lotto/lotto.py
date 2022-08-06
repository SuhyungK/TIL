# 여기에 필요한 모듈을 추가합니다.
import random
import json


class Lotto:

    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        self.n = n
        self.number_lines += [sorted(random.sample(range(1, 46), 6)) for j in range(n)]
        print(self.number_lines)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
    
        date = Lotto.get_draw_date(draw_number)
        print(f"""
=========================================
             제 {draw_number} 회 로또
=========================================
추첨일 : {date[0]}/{date[1]}/{date[2]}
=========================================
""")
        for i in range(self.n):
            print(f"{chr(i+65)} : {self.number_lines[i]}")

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        
        lotto_numbers = Lotto.get_lotto_numbers(draw_number)
        lotto_info = []

        for i in range(self.n):
            lotto_info.append(Lotto.get_same_info(lotto_numbers[0], lotto_numbers[1], self.number_lines[i]))

        lotto_rank = Lotto.get_ranking(lotto_info[0], lotto_info[1])
        print(f"""
=========================================
당첨 번호 : {lotto_numbers[0]} + {lotto_numbers[1]}
=========================================
""")
        for i in range(self.n):
            print(f"{chr(i+65)} : {lotto_info[0][0]}개 일치", end='')
            if lotto_info[0][1]:
                print(' + 보너스 일치',end='')
            print()


    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        _ = open('data/lotto_' + str(draw_number) + '.json', encoding='utf-8')
        detail = json.load(_)['drwNoDate']
        year, month, day = detail.split('-')
    
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        _ = open('data/lotto_' + str(draw_number) + '.json', encoding='utf-8')
        detail2 = json.load(_)
        main_numbers, bonus_number = [], []
        for k, i in detail2.items():
            if k.startswith('drwt'):
                main_numbers.append(i)
        bonus_number = detail2.get('bnusNo')
       
        return sorted(main_numbers), bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False

        for i in range(len(main_numbers)):
            if main_numbers[i] == line[i]:
                same_main_counts += 1
        if bonus_number in line:
            is_bonus = True
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):

        rank = '655432'
        ranking = rank.find(str(same_main_counts)) + 1

        if ranking == 5 and not(is_bonus):
            ranking += 1

        return ranking
