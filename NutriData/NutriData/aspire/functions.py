import math
toph_api_key = 'ffcbb1d69amsh90230347f7931d3p1536aejsn25568159361e'
mckenna_api_key = '33ea8e8ec5msh5b89e2129e49ef7p1ad746jsnc923290b266f'
corban_api_key = '4280b68f46mshaf658c384f5e5a5p1b442bjsn0a6f338351ad'
api_key = mckenna_api_key

def searchRecipes(maxProtein, maxCarbs, maxFat, maxCal, recipe):
    import requests
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
    querystring = {"maxProtein":maxProtein,"maxCarbs":maxCarbs,"maxFat":maxFat,"maxCal":maxCal,"number":"5","query":[recipe], 
    #this is what will be entered in the 'search bar'.
    }
    headers = {
        "X-RapidAPI-Key": "04fb037d86mshbc10cd2bcf9efc3p1b1aa2jsnb5518a2797b1",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    responseSearchRecipe = requests.request("GET", url, headers=headers, params=querystring)
    r = responseSearchRecipe.json()
    #Make a dictionary with the recipe name as the key and the recipe ID as the value
    recipeDict = {}
    for i in r['results']:
        recipeDict[i['title']] = i['id']
    
    return(recipeDict)


#@title Get Recipe Information
def getRecipeInformation(id):
    #The desired ID is then put into another API call to the endpoint GetRecipeInformation
    recipeID = id #change this once we get another input
    recipeID = str(recipeID)

    import requests

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipeID}/information"

    querystring = {"includeNutrition":"true"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    responseGetRecipeInformation = requests.request("GET", url, headers=headers, params=querystring)

    #make a dictionary with the required nutrients
    r = responseGetRecipeInformation.json()
    nutrientDict = {}
    nutrientDict['title'] = r['title']
    nutrientDict['fat']  = math.ceil((r['nutrition']['nutrients'][1]['amount']))
    nutrientDict['protein'] = math.ceil((r['nutrition']['nutrients'][8]['amount']))
    nutrientDict['carbs'] = math.ceil((r['nutrition']['nutrients'][3]['amount']))
    nutrientDict['calories'] = math.ceil((r['nutrition']['nutrients'][0]['amount']))
    
    return nutrientDict

def round(val):
    return int(math.ceil(val))

