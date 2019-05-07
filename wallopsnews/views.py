from django.shortcuts import get_object_or_404, render

from .models import Article

# Create your views here.
from django.http import HttpResponse


def index(request):
    celebrities_list = Article.objects.filter(article_type = "Celebrities")[:2]
    food_list = Article.objects.filter(article_type = "Food")[:2]
    tech_list = Article.objects.filter(article_type = "Tech")[:2]
    travel_list = Article.objects.filter(article_type = "Travel")[:5]
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'wallops/wallopsHome.html', {'latest_article_list': latest_article_list, 'celebrities_list':celebrities_list, 'food_list': food_list,'tech_list': tech_list, 'travel_list':travel_list})

def articleContent(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'wallops/articleTemplate.html', {'article':article, 'latest_article_list': latest_article_list})

