from django.urls import path
from .views import *

app_name = 'health'
urlpatterns = [
    # ex:/
    path('', index, name='index'),
    path('doctor/', doctor, name='doctor'),
    path('pension/', pension, name='pension'),
    path('news/', NewsView.as_view(), name='news'),
    path('industry-news/', IndustryNewsView.as_view(), name='industry-news'),
    path('media/<int:pk>/', MediaView.as_view(), name='media'),
    path('industry/<int:pk>/', IndustryView.as_view(), name='industry'),
    path('contact/', ContactView.as_view(), name='contact'),
]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
