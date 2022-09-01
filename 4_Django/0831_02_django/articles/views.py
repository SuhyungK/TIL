from django.shortcuts import render, redirect
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
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 실제로 DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')
    # 3
    # Article.objects.create(title=title, content=content)
    
    # return render(request, 'articles/index.html')

    # 게시글 상세보기
    # url(variable routing에 사용한 변수)들은 다 함수의 인자로 받음)
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article, 
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # 데이터를 다시 요청해야 할 때는 redirect
    # 화면 전환만 해야 할 때는 render
    return redirect('articles:index')

    # 수정 페이지로 렌더링
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article, 
    }
    return render(request, 'articles/edit.html', context)

    # 수정 적용 
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)