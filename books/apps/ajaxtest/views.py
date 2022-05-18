# from django.conf import settings
from django.shortcuts import render
# from django.contrib.auth.models import User


def index(request):
    context={
        
        }
    return render(request,'ajaxtest/index.html',context)
    
    
     