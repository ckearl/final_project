from django.urls import path
from .views import indexPageView, loginPageView, savedPageView, recipePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),   
    path("register/", loginPageView, name="register"),   
    path("saved/", savedPageView, name="saved"), 
    path("recipe/", recipePageView, name="recipe"), 
]     