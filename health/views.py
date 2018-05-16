from django.shortcuts import render
from django.http import Http404
from .models import Provide, Article, Contact, Service, People, Advantage, Industry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    provide_list = Provide.objects.all()
    service_list = Service.objects.all()
    context = {
        'provide_list': provide_list,
        'service_list': service_list,
       }
    return render(request, 'health/index.html', context)


def doctor(request):
    people_list = People.objects.all()
    advantage = Advantage.objects.all()
    context = {
        'people_list': people_list,
        'advantage': advantage,
    }
    return render(request, 'health/family-doctor.html', context)


def pension(request):

    return render(request, 'health/pension.html')


def news(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 4)

    page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'health/news.html', {'contacts': contacts, })


def industry_news(request):
    industry_list = Industry.objects.all()
    paginator = Paginator(industry_list, 4)

    page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'health/news-industry.html', {'contacts': contacts, })


def media(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("404")

    context = {
        'article': article,
    }
    return render(request, 'health/media.html', context)


def industry(request, industry_id):
    try:
        article = Industry.objects.get(pk=industry_id)
    except Industry.DoesNotExist:
        raise Http404("404")
    context = {
        'article': article,
    }
    return render(request, 'health/industry.html', context)


def contact(request):
    contact_list = Contact.objects.all()
    context = {'contact_list': contact_list, }
    return render(request, 'health/contact.html', context)
