from django.urls import path
from .views import BlogDetail,BlogInfo,UserBlog

urlpatterns = [
    path("blogs/",BlogDetail.as_view()),
    path("blog/<int:id>",BlogInfo.as_view()),
    path("user-blog",UserBlog.as_view())
]