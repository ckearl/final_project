from django.urls import path
from .views import indexPageView, loginPageView, userPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),   
    path("user/", userPageView, name="user"), 
]     