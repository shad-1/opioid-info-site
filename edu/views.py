from django.shortcuts import render
from . import models
from . import forms

ctx = { 
    'view' : 'Standard'
}

# Create your views here.
def index(request):
    return render(request, 'edu/index.html', ctx)

def about(request):
    return render(request, 'edu/about.html', ctx)

def facts(request):
    facts = models.Fact.objects.all()
    for fact in facts:
        if fact.internal_resources:
            fact.associated_articles = fact.internal_resources.all()
    ctx['facts'] = facts
    return render(request, 'edu/facts.html', ctx)

def resources(request, id=None):
    articles = models.Article.objects.all()
    if id:
        article = articles.get(id=id)
        ctx['article'] = article
        return render(request, 'edu/article.html', ctx)
    else:
        ctx['articles'] = articles
        return render(request, 'edu/resources.html', ctx)

def contact(request):
    ctx['form'] = forms.ContactForm()
    return render(request, 'edu/contact.html', ctx)

def community(request):
    return render(request, 'edu/community.html', ctx)

def login(request):
    return render(request, 'shared/login.html', ctx)

def register(request):
    return render(request, 'shared/register.html', ctx)
