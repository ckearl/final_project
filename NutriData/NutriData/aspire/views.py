#### Some changes
## Some other changes
# A third change
# a fourth change 
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('you have succesfully reached the INDEX page') 

def loginPageView(request) :
    return HttpResponse('you have succesfully reached the LOGIN page') 

def userPageView(request) :
    return HttpResponse('you have succesfully reached the USER page') 