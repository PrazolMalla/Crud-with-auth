from django.urls import path
from .views import UserDetail,UserInfo,Login,UserView

urlpatterns = [
    path("user/",UserDetail.as_view(),name="user"),
    path("user/<int:id>",UserInfo.as_view()),
    path("login",Login.as_view()),
    path("decode",UserView.as_view())
]