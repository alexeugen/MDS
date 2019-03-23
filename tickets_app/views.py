# Create your views here.

from django.shortcuts import render

#a list of dictionaries
posts = [
    {
        "titlu" : "The Trail to Oregon",
        "regie" : "Andrei Alexandrescu",
        "actori" : "Mircea, Andrei, Mihai",
        "descriere" : "A comedy about the life of the people who searched for a better life by heading to Oregon",
        "locatie" : "Teatrul Maria Filotti",
        "data" : "23 Septembrie 2019, Ora 13:30",
        "img" : "/imgs/poster1.jpg" ,
        "background": "/imgs/background1.jpg"
    },
    {
        "titlu" : "Firebringer",
        "regie" : "Andrei Alexandrescu",
        "actori" : "Mircea, Alex, Mihai",
        "descriere" : "A comedy about the life of the people who searched for a better life by heading to Oregon A comedy about the life of the people who searched for a better life by heading to Oregon ",
        "locatie" : "Teatrul Maria Filotti",
        "data" : "23 Septembrie 2029, Ora 13:30",
        "img" : "/imgs/poster2.jpg" ,
        "background": "/imgs/background2.jpg"
    }
]

def home(request):
    # context dictionary
    context = {
        'posts': posts
    }
    return render(request, 'tickets_app/home.html', context)
def about(request):
    return render(request, 'tickets_app/about.html')
