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

def registerPageView(request) :
    return render(request, 'aspire/register.html')

def savedUserPageView(request) :
    #this generates a new user obeject using the information received through registering
    new_user = User()
    new_user.firstName = request.POST.get('first_name')
    new_user.lastName = request.POST.get('last_name')
    new_user.email = request.POST.get('inputEmail')
    new_user.password = request.POST.get('inputPassword')

    new_user.save()

    context = {
        'user' : new_user
    }

    return savedPageView(request, new_user.id)

def savedLoginPageView (request) :
    useremail = request.POST.get('email')
    userpassword = request.POST.get('password')

    #checks if the useremail and password match
    try :
        user = User.objects.get(email = useremail, password = userpassword)

    except :

        return render(request, 'health_app/login.html')

    return savedPageView(request, user.id)

def savedPageView(request, user_id=1, recipe_name=None, ingredient_name=None, ingredient_id=None) :

        #search recipes
    if recipe_name != None :
        recipe_dict = searchRecipes(recipe_name)
    else :
        recipe_dict = dict()
<<<<<<< HEAD
=======
    '''
    #search ingredients
    if ingredient_name != None :
        ingredient_dict = searchIngredients(ingredient_name)
    else :
        ingredient_dict = dict()

    #enter measurement for ingredients
    if ingredient_id != None :
        measure_list = getIngredientInformation1(ingredient_id)
    else :
        measure_list = list()
    '''
>>>>>>> de556c953c1e6ddca83b9af3add835fdd2dd4e89

    user = User.objects.get(id = user_id)
    meal_dict = Recipe_User.objects.filter(user = user_id)

    recipe_list = list()
    for meal in meal_dict :
        recipe_list.append(Recipe.objects.get(id = Recipe_User.recipe.id))


    context = {
            'user' : user,
            'ingredient_name' : ingredient_name,
            'recipe_dict' : recipe_dict,
<<<<<<< HEAD
=======
            #'ingredient_dict' : ingredient_dict,
            'ingredient_id' : ingredient_id,
            #'measure_list' : measure_list,
>>>>>>> de556c953c1e6ddca83b9af3add835fdd2dd4e89
        }

    return render(request, 'health_app/dash.html', context)

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

    new_recipe.name = recipe_dict['title']
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


def recipePageView(request) :
    return render(request, 'aspire/recipe.html')

