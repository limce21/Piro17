from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import Post
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        print("들어옴!")
        print(request.POST['interest'])
        post = Post.objects.get(id=request.POST['id'])
        interest = request.POST["interest"]
        print(post.id)
        Post.objects.filter(id=post.id).update(interest=interest)

    
    posts = Post.objects.all()
    sort = request.GET.get('sort','None')
    print(sort)
    if sort == "name":
       posts = posts.order_by("title")
    elif sort == "createAt":
       posts = posts.order_by("created_at")
    elif sort == "updateAt":
       posts = posts.order_by("-updated_at")

    print(posts)

    context = {
        "posts": posts,
    }
    return render(request, template_name="posts/home.html", context=context)


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
        print("create", req_photo)
        content = request.POST["content"]
        interest = request.POST["interest"]
        devTools = request.POST["devTools"]

        Post.objects.create(title=title,
                            interest=interest, devTools=devTools, content=content, photo=req_photo)

        return redirect("/")

    context = {'devTools': Post.TOOL_CHOICE}

    return render(request, template_name="posts/create.html", context=context)


def detail(request, id):
    post = Post.objects.get(id=id)

    print(post)
    context = {
        "post": post
    }
    return render(request, template_name="posts/detail.html", context=context)


def update(request, id):
    print(request.method)
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
        print("update", req_photo)
        content = request.POST["content"]
        interest = request.POST["interest"]
        devTools = request.POST["devTools"]

        Post.objects.filter(id=id).update(
            title=title, interest=interest, devTools=devTools,content=content, photo=req_photo)
        return redirect(f"/post/{id}")

    post = Post.objects.get(id=id)
    context = {
        "post": post,
        "devTools": Post.TOOL_CHOICE
    }
    return render(request, template_name="posts/update.html", context=context)


def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")
