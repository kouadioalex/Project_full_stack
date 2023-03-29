from django.shortcuts import render
from django.http import HttpResponse

from .forms import ArticleCreer
from .models import Article
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse


def article_view(request):
    # order_by('-date_publication'): par ordre de publication l'heure d'enregistrement
    article_general= Article.objects.all().order_by('-date_publication')
    
    return render(request, 'Articles/liste_articles.html',context={'contenu_article': article_general } )

def detail_view(request, detail):
    try:
        article_special= Article.objects.get(slug= detail)
        #return HttpResponse("page d'article")
        return render(request, 'Articles/detail_article.html', context={'diff_article': article_special} )
    except Article.DoesNotExist:
        raise Http404("Erreur, cette page ne correspond par à aucune information ")

def creer_view(request):
    forms= ArticleCreer()
    if request.method == 'POST':
        forms= ArticleCreer(request.POST, request.FILES)
        forms.save()
        return HttpResponseRedirect('/article/')
       #return HttpResponseRedirect(reverse('Articles:article') )
    
    return render(request, 'Articles/creer.html', context={'form':forms })
    #return HttpResponse("ma page de creation d'articles")
    #return render(request, )

 