from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles, 
    }

    return render(request, 'articles/index.html', context)

def new(request):
    # 사용자가 데이터를 저장할 페이지
    return render(request, 'articles/new.html')

def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 실제로 DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)
    
    return render(request, 'articles/create.html')