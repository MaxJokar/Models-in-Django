from turtle import update
from venv import create
from django.db import models
from django.utils import timezone

class ChiefEditor(models.Model):
        name=models.CharField(max_length=50,verbose_name='Name')
        family=models.CharField(max_length=50,verbose_name='family ')
        def __str__(self) :
           return self.name+' '+self.family
        
        
class Publication(models.Model):
        title=models.CharField(max_length=100,verbose_name='Name of Publication')
        chiefEditor=models.OneToOneField(ChiefEditor,on_delete=models.CASCADE,primary_key=True,verbose_name='ChiefEditor')
        def __str__(self):
            return  self.title
    


class Author(models.Model):
    # id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    family=models.CharField(max_length=30)
    slug=models.SlugField(max_length=100)
    age=models.IntegerField(default=20,verbose_name='age')
    is_active=models.BooleanField(default=True,verbose_name='Active/Inactive')
    register_date=models.DateTimeField(default=timezone.now, verbose_name='Date of  regisration ')
    email=models.EmailField(max_length=100,verbose_name='Email ')
    image_name=models.CharField(max_length=200,default='nophoto',null=True,blank='True', verbose_name='Image')
    
    
    def __str__(self) :
        return f"{self.name}\t{self.family}\t{self.age}"
    
    
class Article(models.Model):
    article_title=models.CharField(max_length=300,verbose_name='Article Name')
    slug=models.SlugField(max_length=300)
    article_text=models.TextField(verbose_name='Main Text ')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Date of  creation ')
    published_at=models.DateTimeField(default=timezone.now,verbose_name='Date of  Publication ')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Date of refreshment ')
    is_active=models.BooleanField(default=False,verbose_name='Active/Inactive')
    ARTICLE_STATUS=[
            ('Draft','Pishnevis'),
            ('Publish','Published')
            
        ]
    
    status=models.CharField(max_length=40,choices=ARTICLE_STATUS,default='Draft',verbose_name='Article Situation')
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True ,verbose_name='Writer')
    publication=models.ManyToManyField(Publication,verbose_name='PublicationS/ChiefEditor')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    