from django.shortcuts import render
# Create your views here.
posts =[
    {
        'author': "prashant sagar",
        'title': 'this is jus testing',
        'content': 'hello how are everything going on?',
    },
    {
        'author': "prashant sagar",
        'title': 'this is jus testing',
        'content': 'hello how are everything going on?',
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,"blog/home.html", context)

def about(request):
    return render(request, 'blog/about.html')