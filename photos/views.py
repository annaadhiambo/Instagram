from django.shortcuts import render
from .models import Post, Username



# Create your views here.



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'home.html', context)

def register(request):
    return render(request, 'users/register.html')



def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_username = Username.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message,"username": searched_username})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

