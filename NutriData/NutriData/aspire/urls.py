from django.urls import path
from .views import indexPageView, loginPageView, savedPageView, recipePageView, savedUserPageView, \
    savedLoginPageView, dashboardRecipePageView, addRecipePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),   
    path("register/", loginPageView, name="register"),   
    path("saved/<int:user_id><str:recipe_name><str:ingredient_name><int:ingredient_id>", savedPageView, name="saved"), 
    path("recipe/<int:user_id>", recipePageView, name="recipe"), 
    path("saved_user/", savedUserPageView, name="saved_user"), 
    path("saved_login/", savedLoginPageView, name="saved_login"), 
    path("dash_recipe/<str:user_id>", dashboardRecipePageView, name="dash_recipe"), 
    path("add_recipe/", addRecipePageView, name="add_recipe"), 

]     