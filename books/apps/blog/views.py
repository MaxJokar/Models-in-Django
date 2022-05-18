from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.conf import settings
# from apps.blog.models import Author
from .models import Author


# def index1(request):
#     blogList=[
#         {
#             'imagename':'th.jfif',
#             'blogTitle':'English teacher',
#             'summeryDesctiption':'the students nowadays are more impatient and to grab their attention, teaching methods need to cater to their dynamic thinking process',
#             'registerDate':'05.01.2018'
         
         
#          },
        
#         {
#             'imagename':'th1.jfif',
#             'blogTitle':'Russian Teacher',
#             'summeryDesctiption':'У преподавания языков есть свои проблемы. В большинстве случаев это иностранный язык, который учащийся не может понять из своего окружения,,',
#             'registerDate':'05.11.2015'
         
         
#          },
#         {
#             'imagename':'th4.jfif',
#             'blogTitle':'French Teacher',
#             'summeryDesctiption':'leur base de connaissances senrichit des informations disponibles sur Internet',
#             'registerDate':'12.01.2022'
         
         
#          },
#         {
#             'imagename':'th5.jfif',
#             'blogTitle':'Italian Teacher',
#             'summeryDesctiption':'la generazione attuale ottiene visibilità nel mondo attraverso i social media',
#             'registerDate':'05.01.2018'
         
         
#          },
        
        
    # ]
    
def index2(request):
    authors=Author.objects.all() # load all  datas in our table 
    context={
            'media_url':settings.MEDIA_URL,
            "imagename":'th1.jfif',
            'authors':authors
            # 'blogList':blogList,
            
        
        }

    return render(request,'blog/index2.html',context)

    
    
    
def showAuthors(request):
    authors=Author.objects.all() # load all  datas in our table 
    context={
            'media_url':settings.MEDIA_URL,
            # "imagename":'th1.jfif',
            'authors':authors
            # 'blogList':blogList,
            
        
        }
 
    return render(request,'blog/authors.html',context)


# To have additional information about the  Tutor we can  use  Description section which one href  opens it . 

def authorDetail(request,author_id):
    try:
        
        author=Author.objects.get(id=author_id)
    except Author.DoesNotExist:  
            raise Http404("This Page Does not Exit TTTTT")  
    context={
                'media_url':settings.MEDIA_URL,
            
                'author':author
            

            
            }
        
    return render(request, 'blog/author_detail.html',context)








 