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

class BlogDetail(View):
    @csrf_exempt

    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)

    def get(self,request):
        blog = list(Blogs.objects.values())
        return JsonResponse(blog,status = 200,safe=False)
    
    def post(self,request):
        data = json.loads(request.body)
        author_id = data['author_id']
        author = CustomUser.objects.get(pk=author_id)
        try:
            new_data = Blogs(title=data["title"],desc=data["desc"],author=author)
            new_data.save()
            return JsonResponse({"msg":"blog created"})
        except:
            return JsonResponse({"error":"Not a Valid data"})


class BlogInfo(View):
    @csrf_exempt
    def dispatch(*args, **kwargs):
        return super().dispatch( *args, **kwargs)
    
    def get(self,request,id):
        blog=list(Blogs.objects.filter(pk=id).values())
        return JsonResponse(blog,status=200,safe=False)
    
    def put(self,request,id):
        data = json.loads(request.body)
        try:
            new_user = Blogs.objects.get(pk=id)
            data_key = list(data.keys())
            for key in data_key:
                if key == "title":
                    new_user.title = data[key]
                if key == "desc":
                    new_user.desc = data[key]
                new_user.save()
                return JsonResponse({"update":data},safe=False)
        except Blogs.DoesNotExist:
            return JsonResponse({"error":"blog doesn't exist"},safe=False)
        except:
            return JsonResponse({"error":"not a valid data "},safe=False)
    
    