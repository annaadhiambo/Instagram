from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author':'Anna',
        'title':'Photo Post 1',
        'content':'First post content',
        'date_posted':'April 17,2020'
    },
    {
        'author':'Ruth',
        'title':'Photo Post 2',
        'content':'Second post content',
        'date_posted':'April 24,2020'
    }
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html',{'title':'About'})



