from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context ={
        'name': '马上双十一，点击有惊喜',
    }
    return render(request, 'book/index.html', context=context)
