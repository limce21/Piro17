from unittest import runner
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post

def home(request):
    query = request.GET.get('query', None)
    if query:
        posts = Post.objects.filter(region__contains=query)
    else:
        posts = Post.objects.all()

    context = {
        "posts": posts
    }
    return render(request, template_name="posts/home.html", context=context)
 
def create(request):
   if request.method == "POST":
      print(request.POST)
      title = request.POST['title']
      release_year = request.POST['release_year']
      genre = request.POST['genre']
      rate = request.POST['rate']
      director = request.POST['director']
      main = request.POST['main']
      review = request.POST['review']
      running_time = request.POST['running_time']

      Post.objects.create(title=title, release_year=release_year,
                           genre=genre, rate=rate, director=director, main=main, review=review,running_time=running_time )

      return redirect("/")

   context = {}

   return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request, template_name="posts/detail.html", context=context)
 
def update(request, id):
    if request.method == "POST":
        title = request.POST['title']
        release_year = request.POST['release_year']
        genre = request.POST['genre']
        rate = request.POST['rate']
        director = request.POST['director']
        main = request.POST['main']
        review = request.POST['review']
        running_time = request.POST['running_time']
        
        Post.objects.filter(id=id).update(title=title, release_year=release_year,
                           genre=genre, rate=rate, director=director, main=main, review=review,running_time=running_time)

        return redirect(f"/post/{id}")
     
    elif request.method=="GET":
        post = Post.objects.get(id=id)
        context = {
            "post": post
        }

        return render(request, template_name="posts/update.html", context=context)
        

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")
