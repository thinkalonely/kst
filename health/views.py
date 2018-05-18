from django.shortcuts import render
from .models import Provide, Article, Contact, Service, People, Advantage, Industry
from django.views import generic
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


class NewsView(generic.ListView):
    template_name = 'health/news.html'
    context_object_name = 'article_list'
    paginate_by = 4

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')
    '''
    paginator = Paginator(get_queryset, 4)

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
    '''
    # return render(request, 'health/news.html', {'contacts': contacts, })


class IndustryNewsView(generic.ListView):
    template_name = 'health/news-industry.html'
    context_object_name = 'article_list'
    paginate_by = 4

    def get_queryset(self):
        return Industry.objects.order_by('-pub_date')


class MediaView(generic.DetailView):
    model = Article
    template_name = 'health/media.html'
    '''
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("404")

    context = {
        'article': article,
    }
    return render(request, 'health/media.html', context)
    '''


class IndustryView(generic.DetailView):
    model = Industry
    template_name = 'health/industry.html'


class ContactView(generic.ListView):
    model = Contact
    template_name = 'health/contact.html'


def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')


def permission_denied(request):
    return render(request, '403.html')
