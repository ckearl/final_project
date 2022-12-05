from django.http import HttpResponse
from django.shortcuts import render
from .functions import searchRecipes, getRecipeInformation
from .models import User, Recipe, Folder, Recipe_User
from datetime import datetime
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'aspire/index.html')

def loginPageView(request) :
    return render(request, 'aspire/login.html')

def registerPageView(request, try_again=1) :
    context = {
        'try_again' : try_again
    }
    return render(request, 'aspire/register.html', context)

def savedUserPageView(request) :
    #this generates a new user object using the information received through registering
    new_user = User()
    new_user.firstName = request.POST.get('first_name')
    new_user.lastName = request.POST.get('last_name')
    new_user.email = request.POST.get('inputEmail')
    new_user.password = request.POST.get('inputPassword')
    try :
        new_user.save()
    except :
        return registerPageView(request, 2)

    return savedPageView(request, new_user.id)

def savedLoginPageView (request) :
    useremail = request.POST.get('email')
    userpassword = request.POST.get('password')

    #checks if the useremail and password match
    try :
        user = User.objects.get(email = useremail, password = userpassword)

    except :

        return render(request, 'aspire/login.html')

    return savedPageView(request, user.id)

def savedPageView(request, user_id, recipe_name=None) :
    user = User.objects.get(id = user_id)

    #search recipes
    if recipe_name != None :
        recipe_dict = searchRecipes(recipe_name)
    else :
        recipe_dict = dict()

    recipe_user_dict = Recipe_User.objects.filter(user = user_id)

    recipe_obj_list = list()
    for recipe_user in recipe_user_dict :
        recipe_obj_list.append((Recipe.objects.get(recipeId = recipe_user.recipe.recipeId)))

    context = {
            'user' : user,
            'recipe_obj_list' : recipe_obj_list,
        }

    return render(request, 'aspire/saved.html', context)

#this allows a user to view recipes (search)
def dashboardRecipePageView(request, user_id) :
    user = User.objects.get(id = user_id)
    recipe_name = request.GET['recipe_name']

    return savedPageView(request, user_id, recipe_name=recipe_name)

#this allows a user to add recipes to their record
def addRecipePageView(request, user_id) :
    user = User.objects.get(id = user_id)

    recipe_id = request.POST['selected_recipe']
    recipe_dict = getRecipeInformation(recipe_id)

    new_recipe = Recipe()

    new_recipe.title = recipe_dict['title']
    new_recipe.imgUrl = recipe_dict['imgUrl']
    new_recipe.fat = recipe_dict['fat']
    new_recipe.protein = recipe_dict['protein']
    new_recipe.carbs = recipe_dict['carbs']
    new_recipe.calories = recipe_dict['calories'] 
    new_recipe.save()

    new_recipe_user = Recipe_User()
    new_recipe_user.recipe = new_recipe
    new_recipe_user.user = user
    new_recipe_user.save()

    return savedPageView(request, user_id)


def recipePageView(request, user_id, recipe_id) :
    user = User.objects.get(id = user_id)
    recipe = Recipe.objects.get(recipeId = recipe_id)
    context = {
        'user' : user,
        'recipe' : recipe,
    }
    return render(request, 'aspire/recipe.html', context)

