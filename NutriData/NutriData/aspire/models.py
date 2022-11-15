from django.db import models

class Recipe(models.Model) :
    recipeTitle = models.CharField(max_length= 20)
    recipeImgUrl = models.URLField(max_length= 200)

    def __str__(self) :
        return (self.recipeTitle)

class Account(models.Model) :
    email = models.EmailField(max_length= 100)
    password = models.CharField(max_length= 20)
    firstName = models.CharField(max_length= 20)
    lastName = models.CharField(max_length= 20)
    Recipe = models.ManyToManyField(Recipe, blank= False)

    def __str__(self) :
        return (self.email)
        
class Folder(models.Model) :
    folderName = models.CharField(max_length= 20)
    Recipe = models.ManyToManyField(Recipe, blank= False)

    def __str__(self) :
        return (self.folderName)
