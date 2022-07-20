from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import DevTool, Post
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        post = Post.objects.get(id=request.POST['id'])
        interest = request.POST["interest"]
        Post.objects.filter(id=post.id).update(interest=interest)

    
    posts = Post.objects.all()
    sort = request.GET.get('sort','None')
    if sort == "name":
       posts = posts.order_by("title")
    elif sort == "createAt":
       posts = posts.order_by("created_at")
    elif sort == "updateAt":
       posts = posts.order_by("-updated_at")


    context = {
        "posts": posts,
    }
    return render(request, template_name="posts/home.html", context=context)


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
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

    context = {
        "post": post
    }
    return render(request, template_name="posts/detail.html", context=context)


def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
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

def create_devTool(request):
    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        kind = request.POST["kind"]

        DevTool.objects.create(name=name, content=content, kind=kind)

        return redirect("/dev/")

    context = {}

    return render(request, template_name="posts/devCreate.html", context=context)

def detail_devTool(request, id):
    devtool = DevTool.objects.get(id=id)
    context = {
        "devtool": devtool
    }
    return render(request, template_name="posts/devDetail.html", context=context)

def home_devTool(request):
    devtools = DevTool.objects.all()
    context = {
        "devtools": devtools,
    }
    return render(request, template_name="posts/devHome.html", context=context)

def delete_devTool(request, id):
    if request.method == "POST":
        DevTool.objects.filter(id=id).delete()
        return redirect("/dev/")
    
def update_devTool(request, id):
    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        kind = request.POST["kind"]

        DevTool.objects.filter(id=id).update(name=name, content=content, kind=kind)
        return redirect(f"/tool/{id}")

    devtool = DevTool.objects.get(id=id)
    context = {
        "devtool": devtool,
    }
    return render(request, template_name="posts/devUpdate.html", context=context)