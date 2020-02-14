from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def guest_articles_view(request):
    articles = Paginator(Article.objects.all().order_by('-date'), 2)
    if 'page' in request.GET:
        articles = articles.get_page(request.GET['page'])
    else:
        articles = articles.get_page(1)
    return render(request, 'GuestArticles.html', {'articles': articles})

def guest_article_details(request, article_id):
    return render(request, 'GuestArticleDetails.html',
    {'article': Article.objects.get(id = article_id)})

@login_required(login_url='login')
def all_articles_view(request):
    articles = Paginator(Article.objects.filter
        (author_id = request.user).order_by('-date'), 2)

    if 'page' in request.GET:
        articles = articles.get_page(request.GET['page'])
    else:
        articles = articles.get_page(1)

    if 'query' in request.GET:
        articles = Article.objects.filter(
            Q(title__icontains = request.GET['query']) |
            Q(body__icontains = request.GET['query'])
        )
    return render(request, 'ViewAllArticles.html',
    {'articles': articles})

@login_required(login_url='login')
def create_article_view(request):
    if request.method == 'POST':
        Article(title = request.POST['title'],
        body = request.POST['body'],
        author = request.user).save()
        return redirect('viewallarticles')
    else:
        return render(request, 'CreateNewArticle.html')

@login_required(login_url='login')
def article_details_view(request, article_id):
    return render(request, 'ArticleDetails.html',
    {'article': Article.objects.get(id = article_id)})

@login_required(login_url='login')
def delete_article_view(request, article_id):
    Article.objects.get(id = article_id).delete()
    return redirect('viewallarticles')

@login_required(login_url='login')
def update_article_view(request, article_id):
    if request.method == 'POST':
        a = Article.objects.get(id = article_id)
        a.title = request.POST['title']
        a.body = request.POST['body']
        a.save()
        return redirect('viewallarticles')
    else:
        return render(request, 'UpdateArticle.html',
        {'article': Article.objects.get(id = article_id)})
