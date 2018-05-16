from django.urls import path

from . import views

urlpatterns = [
    # ex:/
    path('', views.index, name='index'),
    path('doctor/', views.doctor, name='doctor'),
    path('pension/', views.pension, name='pension'),
    path('news/', views.news, name='news'),
    path('industry-news/', views.industry_news, name='industry-news'),
    path('media/<int:article_id>/', views.media, name='media'),
    path('industry/<int:industry_id>/', views.industry, name='industry'),
    path('contact/', views.contact, name='contact'),
]
