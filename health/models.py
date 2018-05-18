from django.db import models
from simditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    image = models.CharField('图片Url', max_length=50, default='health/images/jigou-img-01.png')
    title = models.CharField('标题', max_length=200)
    keywords = models.CharField('关键词', max_length=200, default='关键词:')
    desc = models.CharField('摘要', max_length=120)
    content = RichTextField('内容')
    pub_date = models.DateField('发布日期')

    def __str__(self):
        return self.title


class Industry(models.Model):
    image = models.CharField('图片Url', max_length=50, default='health/images/jigou-img-03.png')
    title = models.CharField('标题', max_length=200)
    keywords = models.CharField('关键词', max_length=200)
    desc = models.TextField('摘要', max_length=120, default='')
    content = RichTextField('内容')
    pub_date = models.DateField('发布日期')
    ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField('公司名', max_length=10, default='易讯通')
    contact_phone = models.CharField('联系电话', max_length=12)
    contact_email = models.EmailField('公司邮箱')
    zip_code = models.IntegerField('邮政编码')
    contact_address = models.CharField('公司地址', max_length=50)
    ordering = ['-pub_date']
    # def __str__(self):
    #    return self.name


class Provide(models.Model):
    provide_image = models.CharField('图片Url', max_length=50, default='health/images/icon-01.png')
    provide_title = models.CharField('服务名称', max_length=20)
    provide_text = models.CharField('服务内容', max_length=100)


class Service(models.Model):
    image = models.CharField('图片Url', max_length=50, default='health/images/img-20.png')
    title = models.CharField('服务名称', max_length=20)
    text = models.CharField('服务内容', max_length=100)


class People(models.Model):
    image = models.CharField('图片地址', max_length=100, default='health/images/a.png')
    people = models.CharField('服务人群', max_length=100)


class Advantage(models.Model):
    image = models.CharField('图片地址', max_length=100, default='health/images/a.png')
    advantage = models.CharField('服务优势', max_length=100)

