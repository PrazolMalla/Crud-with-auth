from django.urls import path
from .views import BlogDetail,BlogInfo

urlpatterns = [
    path("blogs/",BlogDetail.as_view()),
    path("blog/<int:id>",BlogInfo.as_view()),
]