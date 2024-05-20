from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Blogs
from django.http import JsonResponse
import json
from user.models import CustomUser 
import jwt


# def token_required(f):
#     def wrap(request, *args, **kwargs):
#         print(request)
#         auth_header = request.headers.get('Authorization')
#         if auth_header is None:
#             return JsonResponse({'error': 'Authorization header missing'}, status=401)
#         try:
#             token = auth_header.split(" ")[1]
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#             request.user_id = payload['id']
#         except:
#             return JsonResponse({'error': 'Invalid token'}, status=401)
#         return f(request, *args, **kwargs)
#     return wrap

class BlogDetail(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)

    def get(self,request):
        blogs = Blogs.objects.values('id', 'title', 'desc', 'author__first_name').filter(isDeleted=False)
        blog_list = list(blogs)
        return JsonResponse(blog_list,status = 200,safe=False)
    
    def post(self,request):
        data = json.loads(request.body)
        access_token = request.headers.get('Authorization').split(' ')[1] 
        print(access_token)
        try:
            access_token_payload=jwt.decode(access_token,'secret',algorithms='HS256')
            author_id = access_token_payload['id']
            author = CustomUser.objects.get(pk=author_id)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"msg":"tokne expired"})
        try:
            new_data = Blogs(title=data["title"],desc=data["desc"],author=author)
            new_data.save()
            return JsonResponse({"msg":"blog created"})
        except:
            return JsonResponse({"error":"Not a Valid data"})


class BlogInfo(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)
    
    def get(self,request,id):
        blog=list(Blogs.objects.filter(pk=id).values())
        return JsonResponse(blog,status=200,safe=False)
    
    def put(self,request,id):
        data = json.loads(request.body)
        print(data)
        try:
            new_blog = Blogs.objects.get(pk=id)
            data_key = list(data.keys())
            for key in data_key:
                if key == "title":
                    new_blog.title = data[key]
                if key == "desc":
                    new_blog.desc = data[key]
                new_blog.save()
                return JsonResponse({"update":data},safe=False)
        except Blogs.DoesNotExist:
            return JsonResponse({"error":"blog doesn't exist"},safe=False)
        except:
            return JsonResponse({"error":"not a valid data "},safe=False)
    
    def delete(self,request,id):
        try:
            blog = Blogs.objects.get(pk=id)
            blog.isDeleted = True
            blog.save()
            return JsonResponse({"msg": "User deleted"}, status=204, safe=False)
        except:
            return JsonResponse({"msg": "User not deleted"}, status=400, safe=False)

    

class UserBlog(View):
    def get(self,request):
       
        access_token = request.headers.get('Authorization').split(' ')[1] 
        try:
            payload = jwt.decode(access_token, 'secret', algorithms=['HS256'])
            author_id = payload['id']
            blogs = Blogs.objects.values('id', 'title', 'desc', 'author__first_name').filter(author_id=author_id ,isDeleted=False)
            blog_list = list(blogs)
            return JsonResponse(blog_list,status = 200,safe=False)
        except:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        
    