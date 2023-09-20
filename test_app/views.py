from django.shortcuts import render, redirect
from django.urls.base import reverse
from .models import News, Category
from .forms import NewsForm, CategoryForm

def main_page(request):
    eng_news = News.objects.filter().order_by("-views")
    search = request.GET.get("soz", None)
    if request.method == "GET" and search != None :
        news = News.objects.filter(titele__contains=search).order_by("-id")
        context = {     
        "news":news,
        "eng_kop": eng_news
        }
        return render(request, "index.html", context)
    else:
        news = News.objects.all().order_by("-id")
        context = {          
            "news":news,
            "eng_kop": eng_news
        }
        return render(request, "index.html", context)

def category_page(request, cat_id):
    news = News.objects.filter(category=cat_id)
    context = {       
        "news":news
    }
    return render(request, "index.html", context)

def batafsil_page(request, id):
    news = News.objects.get(id=id)
    news.views+=1
    news.save()
    context = {
        "news": news,       
    }
    return render(request, "batafsil.html", context)

def add_news_page(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse("home-page"))
    context = {
        "form": form
    }        
    return render(request, "add_news.html", context)

def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("home-page"))
    context = {
        "form": form
    }   
    return render(request, "add_category.html", context)

def admin_page(request):
    news = News.objects.filter()
    context = {
        "news": news
    }
    return render(request, "admin.html", context)

def del_news(request, news_id):
    news = News.objects.get(id=news_id)
    if news:
        news.delete()
    return redirect(reverse("admin-page"))

def news_holati(request, news_id):
    news = News.objects.get(id=news_id)
    if news_id and news.holati==True:
        news.holati = False
        news.save()
    elif news_id and news.holati==False:
        news.holati = True
        news.save()
    return redirect(reverse("admin-page"))
