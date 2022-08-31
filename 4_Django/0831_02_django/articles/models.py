from django.db import models

# Create your models here.
class Article(models.Model):
    # Model이라는 클래스의 모든 속성을 상속받음
    # 여기서는 필드를 정의하기만 함
    # 게시판의 내용과 제목을 작성할 수 있는 데이터베이스를 작성
    
    # 클래스 변수 = 하나의 필드
    # 모델 클래스 == 테이블 스키마
    # 컬럼 - datatype
    # CharField = models안에 있는 타입을 결정하는 무언가...
    # 테이블을 만들기 위한 뼈대 설계
    title = models.CharField(max_length=10)
    content = models.TextField()
    pass
