from django.urls import path
from . import views

app_name='pages'
urlpatterns = [
    # url이 일치했을 때-> 어떤 인자를 참조할 것인가
    # 같은 위치에 있는 views.py(명시적 위치 권장)
    path('index/', views.index, name='index')
]
