import xadmin
from .models import Article, Industry


# class ArticleAdmin(admin.ModelAdmin):
class ArticleAdmin(object):

    list_display = ('title', 'id', 'keywords', 'pub_date')


# class IndustryAdmin(admin.ModelAdmin):
class IndustryAdmin(object):
    list_display = ('title', 'id', 'keywords', 'pub_date')


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Industry, IndustryAdmin)
