# Create your views here.

from django.shortcuts import render

#a list of dictionaries
posts = [
    {
        'author' : 'Andreea',
        'title' : 'Blog post 1',
        'content' : 'First post content',
        'date_posted' : 'March 20, 2018'
    },
    {
        'author': 'Danut',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'March 21, 2018'
    }
]

def home(request):
    #context dictionary
    context = {
        'posts' : posts
    }
    return render(request, 'tickets_app/home.html', context)

def about(request):
    return render(request, 'tickets_app/about.html')
