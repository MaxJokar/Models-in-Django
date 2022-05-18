from django.contrib import admin
from apps.blog.models import Author,Article,Publication,ChiefEditor

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    List_display=('name','family','email','age','register_date')
    List_filter=('family','is_active')
    search_filds=('family','name')
    ordering=['family','name']
    prepopulated_fields={'slug':('name','family')}

# admin.site.register(Author,AuthorAdmin)
# FOR THE ARTICEL WE ALSO WANT TO  ADD  

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    List_display=('article_title','created_at','is_active','status','author')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    List_display=('title','chiefEditor')


@admin.register(ChiefEditor)
class CiefEditorAdmin(admin.ModelAdmin):
    List_display=('name','family','publication')























