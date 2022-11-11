from django.urls import path
from .views import indexPageView, loginPageView, searchPageView, savedPageView, recipePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),   
    path("search/", searchPageView, name="search"), 
    path("saved/", savedPageView, name="saved"), 
    path("recipe/", recipePageView, name="recipe"), 
]     