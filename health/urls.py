from django.urls import path
from .views import *

app_name = 'health'
urlpatterns = [
    # ex:/
    path('', index, name='index'),
    path('doctor/', doctor, name='doctor'),
    path('pension/', pension, name='pension'),
    path('news/', news, name='news'),
    path('industry-news/', industry_news, name='industry-news'),
    path('media/<int:article_id>/', media, name='media'),
    path('industry/<int:industry_id>/', industry, name='industry'),
    path('contact/', contact, name='contact'),
]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
