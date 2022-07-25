from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import Post, Comment
import json

# Create your views here.
def post(request):
   post = Post.objects.get(id=1)
   all_comments = post.comment_user.all()
   comments_count = len(all_comments)

   context= {
      'post': post,
      'comments': all_comments,
      'comments_count': comments_count,
   }
   return render(request, 'pirostagrams/my_post.html', context=context)

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)  
    post_id = req['id']
    button_type = req['type']
    
    post = Post.objects.get(id=post_id)

    if button_type == 0:
        post.like = 1
    else:
        post.like = 0

    post.save()  # db에 꼭 저장을 해줘야 함!
    return JsonResponse({'type': post.like})

@csrf_exempt
def register_comment(request):
   req = json.loads(request.body)
   post_id = req['id']
   content = req['type']
   print(content)
   Comment.objects.create(post_id=post_id, comment=content)
   length = len(Comment.objects.all())
   print(length)
   comments = Comment.objects.all()
   last_comment = comments[length-1]
   last_id = last_comment.id
   print(last_id)
   return JsonResponse({'type':content, 'last_id':last_id})

@csrf_exempt
def delete_comment(request):
   try:
      req = json.loads(request.body)
      comment_id = req['id']
      Comment.objects.filter(id=comment_id).delete()
      return JsonResponse({'id':comment_id})
   except:
      print("error")
      comments = Comment.objects.all()
      last_comment = comments[len(comments)-1]
      last_id = last_comment.id
      Comment.objects.filter(id=last_id).delete()
      return JsonResponse({'id':last_id})
   
   