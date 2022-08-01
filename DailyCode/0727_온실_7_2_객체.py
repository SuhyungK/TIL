# 객체와 클래스 만들기


class Dogs:
    nums_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dogs.nums_of_dogs += 1
        Dogs.birth_of_dogs += 1

    def bark():
        return "개 짖는 소리"

    def __del__(self): # 객체가 없어졌을 때
        Dogs.nums_of_dogs -= 1
    
    @classmethod
    def get_status(cls): # 클래스 함수
        return f'태어난 개의 숫자 : {cls.birth_of_dogs}, 현재 개의 숫자 : {cls.nums_of_dogs}'
        
# 교수님


d1 = Dogs("바둑이", "진돗개")
print(Dogs.get_status(d1))