from django.db import models

class Recipe(models.Model) :
    recipeId = models.IntegerField()
    recipeTitle = models.CharField(max_length= 20)
    recipeImgUrl = models.URLField(max_length= 200)

    def __str__(self) :
        return (self.recipeTitle)

class User(models.Model) :
    email = models.EmailField(max_length= 100)
    password = models.CharField(max_length= 20)
    firstName = models.CharField(max_length= 20)
    lastName = models.CharField(max_length= 20)

    def __str__(self) :
        name = self.firstName + ' ' + self.lastName
        return (name)


class Folder(models.Model) :
    folderName = models.CharField(max_length= 20)

    def __str__(self) :
        return (self.folderName)

class Recipe_User(models.Model) :
    starred = models.BooleanField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self) :
        text = self.user.firstName + ' ' + self.user.lastName + '; ' + self.recipe.recipeTitle 
        return (text)
        