from django.contrib import admin
import xadmin
from .models import Article, Contact, Provide, Service, People, Advantage, Industry


# class ArticleAdmin(admin.ModelAdmin):
class ArticleAdmin(object):

    list_display = ('title', 'id', 'keywords', 'pub_date')


# class IndustryAdmin(admin.ModelAdmin):
class IndustryAdmin(object):
    list_display = ('title', 'id', 'keywords', 'pub_date')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_phone', 'contact_email', 'zip_code', 'contact_address')


class ProvideAdmin(admin.ModelAdmin):
    list_display = ('provide_title', 'provide_text')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'people')
    ordering = ('id',)


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'advantage')
    ordering = ('id',)


# xadmin.site.register(Article, ArticleAdmin)
# xadmin.site.register(Industry, IndustryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Provide, ProvideAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Advantage, AdvantageAdmin)
