from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'aspire/index.html')

def loginPageView(request) :
    return render(request, 'aspire/login.html')

def registerPageView(request) :
    return render(request, 'aspire/register.html')

def searchPageView(request) :
    return render(request, 'aspire/search.html')

def savedPageView(request) :
    return render(request, 'aspire/saved.html')

def recipePageView(request) :
    return render(request, 'aspire/recipe.html')
