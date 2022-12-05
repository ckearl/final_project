from django.urls import path
from .views import indexPageView, loginPageView, savedPageView, recipePageView, savedUserPageView, \
    savedLoginPageView, dashboardRecipePageView, addRecipePageView, registerPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),   
    path("register/", registerPageView, name="register"),   
    path("saved/<int:user_id>/<str:recipe_name>", savedPageView, name="saved"), 
    path("saved/<int:user_id>", savedPageView, name="saved"), 
    path("recipe/<int:user_id>/<int:recipe_id>", recipePageView, name="recipe"), 
    path("saved_user/", savedUserPageView, name="saved_user"), 
    path("saved_login/", savedLoginPageView, name="saved_login"), 
    path("dash_recipe/<str:user_id>", dashboardRecipePageView, name="dash_recipe"), 
    path("add_recipe/", addRecipePageView, name="add_recipe"), 

]     