from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('you have succesfully reached the INDEX page') 

def loginPageView(request) :
    return HttpResponse('you have succesfully reached the LOGIN page') 

def searchPageView(request) :
    return HttpResponse('you have succesfully reached the SEARCH page') 

def savedPageView(request) :
    return HttpResponse('you have succesfully reached the SAVED page') 

def recipePageView(request) :
    return HttpResponse('you have succesfully reached the RECIPE page') 